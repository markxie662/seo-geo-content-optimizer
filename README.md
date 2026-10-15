![SEO/GEO Content Optimizer — 网站内容规划与页面改写](docs/assets/cover.svg)

# SEO/GEO Content Optimizer

**从一个网址，到有证据的整站内容规划与完整页面改稿。**

[![Repository checks](https://github.com/markxie662/seo-geo-content-optimizer/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/markxie662/seo-geo-content-optimizer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-27615B.svg)](LICENSE)

一个面向 Google 搜索和生成式搜索的 Agent Skill。输入网站网址，识别页面职责与内容缺口，排列优化任务，并交付一个重点页面的完整改稿。适用于企业、SaaS、电商、博客和文档站。

*An evidence-led agent skill for website content planning and complete page rewrites. Chinese analysis by default; page copy follows the audience's language.*

[快速开始](#快速开始) · [实际输出](#实际输出) · [方法与边界](#方法与边界) · [验证记录](docs/validation.md) · [参与维护](CONTRIBUTING.md)

## 你会得到什么

| 交付 | 解决的问题 |
|---|---|
| 证据范围 | 读了哪些页面、取得哪些数据、还有什么未验证 |
| 整站内容地图 | 用户任务如何对应现有页面；哪里需要补充、区分或核实 |
| 优先任务与后续队列 | 先改什么、依据是什么、需要哪些素材、如何验收 |
| 重点页面完整稿 | title、meta description、连续正文、已核实内链与下一步行动 |
| 素材需求与复查计划 | 哪些事实需要补证，如何分别观察搜索、AI 引用和有效访问 |

只需要优化一页时，技能会缩小范围。默认报告说明使用中文，页面文案保留目标读者的语言与品牌声音。

## 快速开始

### 1. 安装到 Codex

在 Codex 对话中发送以下**安装请求**，这不是终端命令：

```text
使用 $skill-installer 安装 https://github.com/markxie662/seo-geo-content-optimizer。
仓库根目录就是技能目录。调用 GitHub 安装脚本时明确使用：
--repo markxie662/seo-geo-content-optimizer --ref main --path .
--name seo-geo-content-optimizer --dest "$HOME/.agents/skills"
安装后确认 ~/.agents/skills/seo-geo-content-optimizer/SKILL.md 存在。
```

也可以在仓库的 **Code → Download ZIP** 下载完整目录，解压后将技能文件夹放到 `~/.agents/skills/seo-geo-content-optimizer/`，确保该目录下直接存在 `SKILL.md`。同名目录已有内容时，先保留旧版。

当前 [OpenAI Docs](https://learn.chatgpt.com/docs/build-skills) 将 `~/.agents/skills` 列为用户级技能目录。Codex 会自动检测新技能；未出现时再重启。安装路径与行为核验于 **2026-10-15**。

安装器的 `--dest` 是技能安装基目录，`--name` 是其下的新目录名。安装根目录时需同时指定 `--path .` 和名称，避免推导出无效名称或重复嵌套目录。

<details>
<summary>从旧名称 seo-geo-content 迁移</summary>

仓库和调用名已统一为 `seo-geo-content-optimizer`，新调用为 `$seo-geo-content-optimizer`。GitHub 的仓库改名不会自动更新本机已安装技能。

按上方步骤安装新目录；若旧目录有自定义内容，先备份到技能扫描目录之外。确认新版本可用后，将旧目录移出扫描位置，避免同时选中两个版本。

已有 Git 克隆可更新远程地址，无需重新克隆：

```sh
git remote set-url origin https://github.com/markxie662/seo-geo-content-optimizer.git
```

旧仓库链接按 [GitHub 重命名规则](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository) 重定向，后续请使用新地址。历史测试输入和报告中的旧调用名会保留，以便复查。

</details>

### 2. 给出网址与目标

```text
使用 $seo-geo-content-optimizer 分析 https://example.com，制定整站内容优化规划，
并完整重写最值得优先改进的页面。

目标受众：中小企业采购者
目标市场：英国
业务目标：让读者判断服务是否适合，并发起有效咨询
```

网址是必需输入，其余信息可选。默认抽样深入阅读最多 12 个代表页面；样本与未验证范围会写入报告。报告默认保存在当前工作区的 `outputs/seo-geo/<host>/<日期>/report.md`。

指定改稿页会优先读取并纳入预算；材料不足时保留指定范围，说明可完成部分和补充需求。SEO 覆盖表用于内部自检，完整逐项明细在用户要求时再附上。

单页任务可以这样提：

```text
使用 $seo-geo-content-optimizer 只优化这篇英文教程：<页面网址>。
保留作者声音，提供完整英文正文、中文编辑说明和缺失证据清单。
```

### 3. 运行条件

宿主 Agent 需要能够读取技能文件，具备网页读取或浏览能力，以及报告文件的写入权限。技能没有付费关键词工具、独立 API Key 或 Search Console 账号的前置要求；已有数据可由用户提供或授权读取。无法取得网页正文时，会说明限制与材料需求。

本项目提供的是工作流说明与模板，执行能力来自宿主 Agent。当前安装说明以 Codex 为准。

## 实际输出

下面是初版已经执行过的**离线模拟案例**。公司、产品及 `.example` 域名均为虚构；输入快照和原始输出都已保留，可以逐项对照。改名修订版另有两项实际回归，见[验证记录](docs/validation.md#改名修订版的实际回归)。

| 场景 | 查看输入 | 查看实际报告 | 重点 |
|---|---|---|---|
| 企业服务站 | [四页快照](evals/fixtures/enterprise.md) | [整站规划与服务页全文](evals/reports/enterprise.md) | 没有客户成效材料时，仍能写清真实服务与边界 |
| 大型电商站 | [12 页样本](evals/fixtures/ecommerce.md) | [内容规划与选购页全文](evals/reports/ecommerce.md) | 不把样本外推成全站重复率，不编高流量关键词 |
| 英文博客 | [原始文章](evals/fixtures/blog.md) | [保留声音的完整改稿](evals/reports/blog.md) | 英文页面文案、中文说明，保持单页范围 |
| 全站无法读取 | [访问限制](evals/fixtures/unavailable.md) | [材料需求与交接](evals/reports/unavailable.md) | 没有正文时不虚构诊断或全文 |

另有产品页和文档站案例。全部六组的条件、历史基线和复核方式见 [验证记录](docs/validation.md)与[机器可读清单](evals/cases.json)。这些材料不构成真实搜索效果或统计基准。

## 方法与边界

### 每种结论都有对应证据

| 类型 | 怎样处理 |
|---|---|
| 页面观察 | 指向具体 URL 和已读取内容；站方自述与独立验证分开 |
| 官方条件 | 标注平台、直接来源及核验日期；满足资格不保证展示 |
| 官方建议 | 按受众任务和站型采用，不升级为强制规则或排名因素 |
| 待验证假设 | 说明推断依据和验证方法，不生成虚构数据 |

优先提供原创信息、真实经验、清晰表达和适用边界。标题、表格、步骤与 FAQ 按读者需要选择；不规定关键词密度、固定字数或固定标题数量，也不把 `llms.txt`、FAQ schema、AI 专版当作通用门槛。

### SEO 与 GEO 共用一份面向读者的内容

覆盖 Google 搜索及 AI 功能、ChatGPT Search、Bing/Copilot、Perplexity，按各平台官方说明分别判断。搜索抓取、模型训练和用户触发访问的用途不混用，也不会为了优化可见性自动开放训练权限。

默认交付内容与建议，不直接修改网站、CMS、爬虫或后台设置。技术交接以实际证据为依据：工具收到 403 不等于搜索爬虫被挡，公开可读取也不等于已索引。技能不保证收录、排名、富结果、AI 引用或转化提升。

### 官方资料与版本状态

- [Google SEO 入门指南](https://developers.google.com/search/docs/fundamentals/seo-starter-guide?hl=zh-cn) → [全部正文章节覆盖表与误区](references/seo-guide-coverage.md)
- [Google 内容质量指南](https://developers.google.com/search/docs/fundamentals/creating-helpful-content?hl=zh-cn) → [内容规划与改稿方法](references/content-strategy.md)
- [Google AI 优化指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)及各平台官方说明 → [GEO 平台差异与来源状态](references/geo-platforms.md)
- 平台报告、指标与实验限制 → [证据与测量](references/evidence-and-measurement.md)

参考资料最近整理核验于 **2026-10-15**，记录了 Google 新旧页面差异及部分 Bing 帮助页的读取限制。使用时仍需刷新涉及的动态规则；未成功复核的事项会标明日期与限制。

本项目独立维护。引用官方资料用于说明方法依据，不表示获得相应机构认证或背书。

## 怎样验证这个仓库

CI 检查技能元数据、包内 Markdown 文件链接和离线案例清单，并运行检查器的行为测试；不调用模型、爬取网站或测试真实搜索效果。

维护者可在 Python 3.10+ 环境运行：

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_repository.py
python -m unittest discover -s tests -v
```

运行结果见 [GitHub Actions](https://github.com/markxie662/seo-geo-content-optimizer/actions/workflows/validate.yml)。自动检查与独立代理的定性验收分别记录，详情见 [验证记录](docs/validation.md)。

## 仓库导航

- [SKILL.md](SKILL.md)：供 Agent 加载的技能入口。
- [agents/openai.yaml](agents/openai.yaml)：显示信息与调用策略。
- [报告模板](assets/report-template.md)：实际交付结构。
- `references/`：按需读取的方法与平台参考。
- `evals/`：历史模拟输入、实际报告与验收点。
- [CONTRIBUTING.md](CONTRIBUTING.md)：纠错、贡献与重新验证方式。

## 许可与维护

由 [@markxie662](https://github.com/markxie662) 维护，原创内容采用 [MIT License](LICENSE)。引用资料与第三方商标保留各自的权利与许可。

发现内容误判、安装问题或官方规则变化，请[提交 Issue](https://github.com/markxie662/seo-geo-content-optimizer/issues/new/choose)，附复现材料或官方来源；贡献方法见 [CONTRIBUTING.md](CONTRIBUTING.md)。
