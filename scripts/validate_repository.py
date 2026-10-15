"""Validate repository metadata, local Markdown links and archived case paths."""
import argparse
from datetime import date
import json
from pathlib import Path
import re
from urllib.parse import unquote

import yaml


SKIP = {".git", ".venv", "outputs", "__pycache__"}


def markdown_targets(text):
    visible, fence = [], None
    for line in text.splitlines():
        candidate = re.sub(r"^ {0,3}(?:[-+*]|\d+[.)]) +", "", line)
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", candidate)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
        elif marker:
            fence = marker[1]
        elif not line.startswith(("    ", "\t")):
            visible.append(line)
    text = re.sub(r"(?<!`)(`+)(?!`).*?(?<!`)\1(?!`)", "", "\n".join(visible), flags=re.S)
    # Overlapping matches retain both destinations in a linked image.
    pattern = r"(?=(?<!\\)\[(?:[^\[\]\n]|\[[^]\n]*\])*\]\(\s*(<[^>]*>|(?:\\.|[^()\s]|\([^()]*\))+))"
    definitions = r"(?m)^ {0,3}\[(?!\^)[^]\n]+\]:\s*(<[^>]*>|\S+)"
    return re.findall(pattern, text) + re.findall(definitions, text)


def validate(root):
    root, errors = Path(root).resolve(), []

    def error(field, message):
        errors.append(f"{field}: {message}")

    def load(relative, parser):
        try:
            result = parser((root / relative).read_text(encoding="utf-8"))
            if not isinstance(result, dict):
                raise ValueError("expected a mapping")
            return result
        except (OSError, ValueError, yaml.YAMLError) as exc:
            error(relative, str(exc).splitlines()[0])
            return {}

    def front_matter(text):
        match = re.match(r"\A---\s*\n(.*?)\n---(?:\s|$)", text, re.S)
        if not match:
            raise ValueError("missing YAML front matter")
        return yaml.safe_load(match[1])

    skill = load("SKILL.md", front_matter)
    if skill.get("name") != "seo-geo-content":
        error("SKILL.md/name", "must be seo-geo-content (lowercase hyphenated name)")
    description = skill.get("description")
    if not isinstance(description, str) or not description.strip():
        error("SKILL.md/description", "must be a nonempty string")
    agent = load("agents/openai.yaml", yaml.safe_load)
    interface, policy = agent.get("interface"), agent.get("policy")
    prompt = interface.get("default_prompt") if isinstance(interface, dict) else None
    if not isinstance(prompt, str) or "$seo-geo-content" not in prompt:
        error("agents/openai.yaml/interface.default_prompt", "must include $seo-geo-content")
    if not isinstance(policy, dict) or policy.get("allow_implicit_invocation") is not True:
        error("agents/openai.yaml/policy.allow_implicit_invocation", "must be boolean true")

    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if SKIP.intersection(relative.parts) or relative.parts[:2] == ("evals", "fixtures"):
            continue
        for target in markdown_targets(path.read_text(encoding="utf-8")):
            target = target[1:-1] if target.startswith("<") else target
            if re.match(r"(?:[a-z][a-z0-9+.-]*:|[/#?])", target, re.I):
                continue
            target = unquote(re.sub(r"\\([\\() ])", r"\1", target.split("#")[0].split("?")[0]))
            destination = (path.parent / target).resolve()
            if not destination.is_relative_to(root) or not destination.exists():
                error(relative, f"broken local link: {target}")

    manifest = load("evals/cases.json", json.loads)
    commit = manifest.get("baseline_skill_commit")
    if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-fA-F]{40}", commit):
        error("evals/cases.json/baseline_skill_commit", "must be a 40-character hex commit")
    evaluated = manifest.get("evaluated_on")
    try:
        if not isinstance(evaluated, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", evaluated):
            raise ValueError()
        date.fromisoformat(evaluated)
    except ValueError:
        error("evals/cases.json/evaluated_on", "must be an ISO date (YYYY-MM-DD)")
    cases = manifest.get("cases")
    if not isinstance(cases, list) or not cases:
        error("evals/cases.json/cases", "must be a nonempty list")
        cases = []
    seen, evals = set(), (root / "evals").resolve()
    for index, case in enumerate(cases):
        label = f"evals/cases.json/cases[{index}]"
        if not isinstance(case, dict):
            error(label, "must be a mapping")
            continue
        for field in ("id", "scope"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                error(f"{label}.{field}", "must be a nonempty string")
        identity = case.get("id")
        if isinstance(identity, str):
            if identity in seen:
                error(f"{label}.id", f"duplicate case ID: {identity}")
            seen.add(identity)
        checks = case.get("checks")
        if not isinstance(checks, list) or not checks or any(not isinstance(c, str) or not c.strip() for c in checks):
            error(f"{label}.checks", "must be a nonempty list of nonempty strings")
        for field in ("fixture", "report"):
            value = case.get(field)
            if not isinstance(value, str) or not value or "\\" in value or Path(value).is_absolute():
                error(f"{label}.{field}", "must be a relative path within evals/")
                continue
            destination = (evals / value).resolve()
            if not destination.is_relative_to(evals) or not destination.is_file() or not destination.stat().st_size:
                error(f"{label}.{field}", "must reference a nonempty file within evals/")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo_root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    errors = validate(parser.parse_args(argv).repo_root)
    print("\n".join(errors) if errors else "Repository checks passed.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
