"""Repository checks use small independent repositories, never model outputs."""
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from scripts import validate_repository as checker


class RepositoryChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("SKILL.md", "---\nname: seo-geo-content\ndescription: Content planning\n---\n# Skill\n")
        self.write("agents/openai.yaml", "interface:\n  default_prompt: Use $seo-geo-content\npolicy:\n  allow_implicit_invocation: true\n")
        self.write("evals/fixtures/example.md", "[simulated](/not-in-the-repo)\n")
        self.write("evals/reports/example.md", "An archived report.\n")
        self.case = dict(id="example", fixture="fixtures/example.md", report="reports/example.md", scope="One page", checks=["Review scope"])
        self.manifest = dict(baseline_skill_commit="a" * 40, evaluated_on="2026-10-15", cases=[self.case])
        self.save_manifest()

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def save_manifest(self):
        self.write("evals/cases.json", json.dumps(self.manifest))

    def errors(self):
        return "\n".join(checker.validate(self.root))

    def test_valid_links_templates_and_code_examples(self):
        self.write("assets/image (one).png", "image")
        self.write("guide.md", "# Guide\n")
        self.write("assets/space image.png", "image")
        self.write("README.md", '[guide](guide.md#unknown) ![image](<assets/image (one).png>)\n[ref][local]\n[local]: guide.md "Title"\n[web](https://example.invalid) [mail](mailto:a@example.invalid)\n[section](#anything) ![encoded](assets/space%20image.png)\n`[example](missing.md)`\n``[nested ` example](missing.md)``\n```md\n[example](missing.md)\n```\n~~~\n![example](missing.png)\n~~~\n    [indented](missing.md)\n{{template}}\n')
        for directory in [".git", ".venv", "outputs", "__pycache__"]:
            self.write(f"{directory}/ignored.md", "[bad](missing.md)")
        self.assertEqual(checker.validate(self.root), [])

    def test_broken_markdown_links_and_images(self):
        for link in ["[bad](missing.md)", "![bad](missing.png)", "[x][ref]\n[ref]: missing.md"]:
            with self.subTest(link=link):
                self.write("README.md", link)
                self.assertIn("README.md", self.errors())
                self.assertIn("missing", self.errors())

    def test_list_fence_does_not_hide_later_links(self):
        self.write("README.md", "- ```md\n  [example](example-only.md)\n  ```\n[real](missing.md)\n")
        self.assertIn("missing.md", self.errors())
        self.assertNotIn("example-only.md", self.errors())

    def test_unmatched_backticks_do_not_hide_links(self):
        self.write("README.md", "`[real](missing.md)``")
        self.assertIn("missing.md", self.errors())

    def test_linked_image_checks_outer_destination(self):
        self.write("image.png", "image")
        self.write("README.md", "[![preview](image.png)](missing.md)")
        self.assertIn("missing.md", self.errors())

    def test_metadata_missing_invalid_or_unsafe_yaml(self):
        for text in ["No front matter", "---\nname: [\n---", "---\nname: !!python/object:bad {}\n---", "---\nname: Bad_Name\n---", "---\nname: another-skill\ndescription: ok\n---", "---\nname: seo-geo-content\ndescription: []\n---"]:
            with self.subTest(text=text):
                self.write("SKILL.md", text)
                self.assertIn("SKILL.md", self.errors())

    def test_interface_prompt_and_implicit_invocation(self):
        for text in ["interface: [", "[]", "interface: {}\npolicy:\n  allow_implicit_invocation: false", "interface:\n  default_prompt: Use another skill\npolicy:\n  allow_implicit_invocation: 'true'"]:
            with self.subTest(text=text):
                self.write("agents/openai.yaml", text)
                self.assertIn("agents/openai.yaml", self.errors())

    def test_missing_required_files(self):
        for name in ["SKILL.md", "agents/openai.yaml", "evals/cases.json"]:
            path = self.root / name
            original = path.read_text()
            path.unlink()
            with self.subTest(name=name):
                self.assertIn(name, self.errors())
            path.write_text(original)

    def test_manifest_format_and_top_level_fields(self):
        for text in ["{", "[]", "{}"]:
            self.write("evals/cases.json", text)
            self.assertIn("evals/cases.json", self.errors())
        for field, value in [("baseline_skill_commit", "short"), ("evaluated_on", "2026-02-30"), ("evaluated_on", "20261015"), ("cases", [])]:
            with self.subTest(field=field, value=value):
                old = self.manifest[field]
                self.manifest[field] = value
                self.save_manifest()
                self.assertIn(field, self.errors())
                self.manifest[field] = old

    def test_manifest_case_fields_and_duplicate_ids(self):
        for field in tuple(self.case):
            with self.subTest(field=field):
                original = self.case.pop(field)
                self.save_manifest()
                self.assertIn(field, self.errors())
                self.case[field] = original
        self.manifest["cases"] = [self.case, dict(self.case)]
        self.save_manifest()
        self.assertIn("duplicate", self.errors())

    def test_manifest_missing_empty_and_escaping_paths(self):
        self.write("outside.md", "exists outside evals")
        self.write("evals/empty.md", "")
        (self.root / "evals/escape.md").symlink_to(self.root / "outside.md")
        for value in ["missing.md", "empty.md", "../outside.md", str(self.root / "outside.md"), "escape.md"]:
            with self.subTest(value=value):
                self.case["report"] = value
                self.save_manifest()
                self.assertIn("report", self.errors())

    def test_cli_success_failure_and_default_root(self):
        with patch.object(checker, "__file__", str(self.root / "scripts/validate_repository.py")), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(checker.main([]), 0)
        self.write("README.md", "[broken](missing.md)")
        result = subprocess.run([sys.executable, checker.__file__, str(self.root)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("README.md", result.stdout)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
