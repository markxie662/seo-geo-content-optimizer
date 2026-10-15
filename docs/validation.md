# 验证记录与离线案例

本页记录实际完成的检查及保留材料，不将案例输出当作搜索效果证明。

- 初版技能基线：[c350661dd37e8d84bf5d3ca29307256a4b3fe9b5](https://github.com/markxie662/seo-geo-content-optimizer/commit/c350661dd37e8d84bf5d3ca29307256a4b3fe9b5)。
- 六组离线执行日期：2026-10-15，Asia/Shanghai。
- 方法：独立代理根据模拟网站快照与原始用户请求执行技能，定性检查范围控制、事实边界和交付行为；不访问真实网站、搜索服务或后台。
- 运行模型、推理强度与采样参数未记录。原始输入和报告逐字节归档，本轮整理没有重新执行六案例或润色原报告。
- 机器可读索引：[evals/cases.json](../evals/cases.json)。路径相对 `evals/`；`checks` 是逐项复核目标，不是自动评分或已通过断言。

历史基线的技能名称为 `seo-geo-content`，当前名称为 `seo-geo-content-optimizer`。输入和报告保留当时的调用名与文字，不通过全局替换改写历史结果。下表是初版基线记录，不自动证明当前修订版具有相同输出。

## 已完成的检查

初版与本轮均执行过官方 skill-creator 的基础结构校验，返回 `Skill is valid!`。检查包括 `SKILL.md` 是否存在、YAML front matter、名称和描述字段要求，以及未完成的 TODO 占位。该校验需要 Python 与 PyYAML，不验证文案质量或搜索效果。

初版七个分发文件已核对包内相对引用，无缺失引用或本机外部文件依赖。公开上传前检查了个人绝对路径和常见凭据模式；本次归档对十二份案例输入、报告重复进行相应扫描，未发现匹配。此类静态检查不等同于完整安全审计。

六份报告来自实际完成的独立代理离线执行。它们保留了输出正文、证据说明与未验证项，可直接对照输入和清单复核；没有保存逐项数值评分、统计通过率或模型对照实验，因此不发布这些指标。

## 可运行的仓库检查

当前仓库另提供 [检查器](../scripts/validate_repository.py)与[行为测试](../tests/test_validate_repository.py)，由 [GitHub Actions](https://github.com/markxie662/seo-geo-content-optimizer/actions/workflows/validate.yml) 在推送及 Pull Request 时运行。安装 [开发依赖](../requirements-dev.txt) 后可在本地复核，命令见 [README](../README.md#怎样验证这个仓库)。

自动检查验证技能元数据、本仓库 Markdown 文件链接的目标，以及初版案例清单的格式、唯一 ID、材料路径唯一性与归档目录对应关系；材料须是可读取、去除空白后非空的 UTF-8 文本。代码片段与 `evals/fixtures/` 中的模拟网站输入不当作仓库链接。链接检查只覆盖有限 Markdown 语法，不联网检查外部网址或锚点，不给报告内容评分，也不重跑模型案例。检查器测试及其覆盖率只能说明检查代码的已测行为，不能表示技能的 SEO/GEO 成功率。

## 改名修订版的实际回归

2026-10-15，另一个独立代理在新的上下文中读取当前技能与参考文件，只使用离线材料，完成了以下两项任务。原始输入和输出未经润色，与初版六案例分开归档。

| 任务 | 输入 | 实际输出 | 人工复核结果 |
|---|---|---|---|
| 指定定价页返回 403，只有 About 页可用 | [输入](../evals/regressions/2026-10-15/specified-page.md) | [报告](../evals/regressions/2026-10-15/specified-page-report.md) | 保留指定页范围，没有换成 About 改稿；未生成价格、元数据或无依据的全文；给出材料需求 |
| 四页企业站规划与指定服务页改稿 | [输入](../evals/regressions/2026-10-15/content-plan.md) | [报告](../evals/regressions/2026-10-15/content-plan-report.md) | 有内容地图、三项优先任务和完整正文；未自动附整张内部自检表；未添加客户、价格或成效数字 |

两份报告均区分了本地参考日期与本次在线核验，未联网，也未声称搜索效果已改善。执行时的八个分发文件版本见 [SHA-256 清单](../evals/regressions/2026-10-15/skill-files.sha256)，路径相对仓库根目录。宿主未提供准确模型标识与采样参数，本次没有记录这些信息。这是两项定性回归，不能推导统计通过率，也不能替代真实网站与平台测试。

## 案例与原始输出

| ID | 原始任务范围与覆盖情形 | 输入 | 原始报告 |
|---|---|---|---|
| `enterprise` | 四页企业服务站的整站规划与中文重点页改稿；抓取与训练选择、有限商业证据 | [fixture](../evals/fixtures/enterprise.md) | [report](../evals/reports/enterprise.md) |
| `ecommerce` | 5,000 条 sitemap 记录中抽样 12 页；选购页改稿、重复率与高流量词请求、局部 canonical 证据 | [fixture](../evals/fixtures/ecommerce.md) | [report](../evals/reports/ecommerce.md) |
| `blog` | 仅改一篇英文散文；保留作者声音、未修复事实与安全边界，避免销售导向 | [fixture](../evals/fixtures/blog.md) | [report](../evals/reports/blog.md) |
| `docs` | 文档规划与英文安装页；版本与命令、明确 noindex、工具 403、新旧方法资料 | [fixture](../evals/fixtures/docs.md) | [report](../evals/reports/docs.md) |
| `product` | 仅改英文产品页；文字转录与音频能力区分、日期化价格、系统与功能限制 | [fixture](../evals/fixtures/product.md) | [report](../evals/reports/product.md) |
| `unavailable` | 完全没有可读正文；拒绝虚构诊断和全文，说明最小补充材料与工具限制 | [fixture](../evals/fixtures/unavailable.md) | [report](../evals/reports/unavailable.md) |

各案例的具体验收点见 [cases.json](../evals/cases.json)。报告中出现的 `.example` 站点、公司与产品均用于模拟；文档中的演示安装命令不是经过验证的真实产品安装建议。

## 如何复查与重跑

1. 在独立目录取得上述技能基线，读取 `SKILL.md` 及其按需参考材料。
2. 为每个案例使用独立上下文，将 fixture 中“用户任务”作为请求，将其余部分作为本次可用读取材料；遵守不联网及材料范围限制。
3. 将新输出与原始报告分开保存，按该案例的 `checks` 逐项定性比较；记录实际模型、参数、日期、技能 commit 和偏差，不覆盖现有基线报告。

复查当前版本时，明确调用 `$seo-geo-content-optimizer`，将历史 fixture 作为请求与输入材料，不因其中的旧调用名切换到旧技能。记录当前技能 commit；结果与初版基线分开保存。

同一请求可以重跑，但原执行参数缺失且模型具有输出差异，不能承诺逐字复现。此案例集不覆盖真实网页发现、浏览器渲染、账户权限、实时平台规则或真实搜索表现；也不是模型统计基准。它不能证明收录、排名、AI 引用、点击或转化提升，后续技能更新亦不能自动继承这些历史执行结果。
