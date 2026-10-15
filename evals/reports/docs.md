# Quartz 2 文档：内容规划与安装页完整改稿

报告与离线材料阅读日期：2026-10-15，Asia/Shanghai。  
入口：https://quartz.example/docs  
目标：让读者完成安装；判断 AI 搜索可见性所需的内容与资格条件。  
语言：报告说明用中文；全部拟发布页面正文、title 与 description 用英语。目标地区未提供。

## 1. 证据范围与主要判断

安装页已经具备完成任务的关键事实：Python 3.11+、macOS/Linux、锁定的 2.0.0 安装命令、版本检查、预期结果、首次格式化命令与不会覆写输入文件的说明。重写应当把这些事实排成可执行的顺序，保留不支持 Windows 的边界，而不是扩充未经验证的性能或安装时长。

最明确的搜索资格风险是安装页提供的 `noindex`；它与希望读者从搜索找到安装说明的目标可能冲突，需要负责人确认意图。本次工具读取安装页为 200，不等于它已索引或能进入 Google AI 搜索。参考页的 403 只证明材料中该读取工具未读到，不能直接宣布 Googlebot、OAI-SearchBot 或其他机器人也被挡。

| 项目 | 本次范围与限制 |
|---|---|
| 发现路径 | 提供的文档导航，发现 /docs、/docs/install、/docs/reference、/docs/troubleshoot |
| 成功深入阅读 | 3 页完整正文，全部可读页已阅读；失败页不计为已读正文 |
| 无法读取 | /docs/reference 返回本次工具 HTTP 403，正文未知；未做其他客户端/爬虫测试 |
| 可用数据 | 无后台、查询、分析、索引或 AI 报表数据 |
| 未知 | robots.txt、响应头、其他摘要控制、实际爬虫访问、索引、Google AI inclusion 与 property 继承、Bing/其他AI采用 |
| 本次操作 | 仅分析用户提供的离线文本；未联网、运行安装命令、访问真实网址、修改网站或后台 |
| 方法时效 | 参考资料标注核验日 2026-10-15；本次同日离线阅读，不是重新访问官方文档；动态规则当前待复核 |

| URL | 用途 | 阅读范围与材料日期 | 选择理由/限制 |
|---|---|---|---|
| https://quartz.example/docs | 版本与导航概览 | 完整正文、title、HTTP 200；2026-10-15 | 定义 Quartz 为虚构本地文本格式化工具，文档覆盖 v2 |
| https://quartz.example/docs/install | 安装与首次运行 | 完整正文、title、noindex、HTTP 200；同日 | 用户指定页，步骤与预期输出可核对 |
| https://quartz.example/docs/troubleshoot | command not found 排错 | 完整正文、title、HTTP 200；同日 | 安装页已有相关链接，保留环境/PATH与勿删文件的提示 |
| https://quartz.example/docs/reference | 参考页 | 只有 HTTP 403；同日 | 已发现但正文未读，不评价其内容是否充分、重复或过时 |

产品能力、命令与支持范围来自站方材料，未进行软件实测。正文会忠实使用这些事实，不声称命令已由本报告验证。

## 2. 定位与内容地图

这是一个面向 Quartz 2 使用者的文档站。材料未表明专业程度、市场或更具体读者画像，按需要安装并首次运行工具的读者组织内容。成功动作是正确安装、识别版本、执行一次格式化命令；不添加销售 CTA。

| 用户任务/候选问法 | 证据类型 | 主题与页面职责 | 现有 URL | 状态与建议 | 下一步行动 |
|---|---|---|---|---|---|
| “这是哪个工具、哪个版本的文档？” | 页面观察；问法为推断 | 概览说明本地文本格式化与 v2 适用范围 | https://quartz.example/docs | 保留版本和三条任务导航；不声称已介绍未知参考参数 | 打开安装页 |
| “怎样安装，并确认安装成功？” | 页面观察 | 安装页提供前提、安装、核对版本、首次运行 | https://quartz.example/docs/install | 完整改稿；noindex 另列技术依赖 | 运行版本检查与格式化命令 |
| “为什么找不到 quartz-demo 命令？” | 页面观察 | 排错页解释同一 Python 环境与 PATH | https://quartz.example/docs/troubleshoot | 将已有两项检查写清楚；保留不要删输入文件 | 核对环境、PATH后重试 |
| “具体参数/命令如何使用？” | 推断；只知道参考页存在 | 参考页职责待实读确认 | https://quartz.example/docs/reference | 先解决本次读取限制，再评价覆盖；不得先建第二份参考页 | 获取正文后确认任务与现有内容 |

安装与排错页有必要交叉引荐，不因共同提到 PATH 就判断关键词竞争。参考信息是否缺失目前未知。现有四个入口已覆盖概览、安装、排错、参考四类用途，没有证据支持批量增加“AI 问题变体”页面。

## 3. 优先任务与后续队列

### 1. 核实安装页 noindex 的意图及实际索引条件

- 页面：https://quartz.example/docs/install。
- 证据：材料中的 `<meta name="robots" content="noindex">`，读取为 HTTP 200，日期 2026-10-15。
- 影响与排序：这是明确控制指令，先于措辞优化影响搜索资格；但是否是错误配置仍需确认。核查成本小，实际调整由有权限人员完成。
- 具体动作：向负责人确认安装页是否意图公开供搜索发现；如果是，检查原始与渲染 HTML、响应头以及 robots 抓取条件，再通过正常发布流程处理冲突的 noindex。若是有意排除，则保留，并记录对搜索目标的取舍。本报告不直接修改它。
- 方法依据：Google [noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing?hl=zh-cn) 为官方控制条件；[robots 说明](https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=en) 区分抓取与索引。均仅按技能离线参考使用，非本次新核验。
- 依赖：有权限负责人确认意图；URL Inspection/相关抓取证据；不能用“普通工具能读”代替。
- 验证：确认指令实际状态、相关抓取工具是否能读到；后续查看所选 canonical 与索引状态。移除指令也不保证索引或引用。

### 2. 发布一份可按顺序完成的英文安装说明

- 页面：https://quartz.example/docs/install。
- 证据：原文已提供完整基础命令，但 title 仅“Install”，首轮任务信息可集中排列。
- 影响与排序：直接对应首要目标，事实足够，编辑成本小；与技术核查并行完成。
- 修改：采用第 4 节；明确支持系统、Python 与版本，安装后给预期输出，再说明首次格式化的行为与排错入口。
- 方法依据：Google [实用内容建议](https://developers.google.com/search/docs/fundamentals/creating-helpful-content?hl=zh-cn) 与 [标题](https://developers.google.com/search/docs/appearance/title-link?hl=zh-cn)/[摘要](https://developers.google.com/search/docs/appearance/snippet?hl=zh-cn) 官方建议；步骤排列是基于本次读者任务的编辑判断。
- 依赖：负责人确认文档事实仍适用 2.0.0；本次没有实测环境。无需虚构安装时长、性能或替代安装方法。
- 验证：逐字核对命令、版本和输出；发布前在真实支持环境由维护者执行安装—检查—首次运行，记录环境与结果。软件不存在于本次授权测试环境，未执行。

### 3. 复核参考页读取失败，避免把未知内容当作缺口

- 页面：https://quartz.example/docs/reference；相关导航 https://quartz.example/docs。
- 证据：只有本次读取工具 403，无正文或其他爬虫测试。
- 影响与排序：可能影响读者查参数，也可能只是工具差异，影响范围未知；核查成本随原因而定。
- 修改：由维护者以正常浏览器与被授权的诊断方式查看；结合具体请求与日志确认是否为预期访问控制，再决定处理。获取正文后再审校版本、参数和安装页衔接。
- 方法依据：官方技术资格与抓取规则须按平台判断；“工具失败不等于爬虫失败”是证据边界。来源见附录 B。
- 依赖：正文或访问诊断资料；不自动放开访问控制、WAF 或训练权限。
- 验证：记录客户端、时间、状态及实际正文；若有明确搜索机器人问题才进一步交接，不能伪造已恢复结果。

### 4. 用实际账户状态与当前功能资料替代旧版 AI 笔记推断

- 页面/设置：文档各页与对应 Search Console property；Bing 等平台仅在实际要评估时核查。
- 证据：团队只有 2025-12-31 中文页摘录；没有新文档或账户设置。技能参考提供了较新的英文指南与独立控制/报告帮助页摘要，但本次禁止联网。
- 影响与排序：避免“无需额外优化”被误读成已经获得资格；也避免把旧 Web 总体统计等同于当前唯一口径。成本小到中，需有权限人员与新资料。
- 修改：按第 6 节列的条件核对索引、摘要资格和 AI inclusion；确认 property 继承状态；保留旧/新来源差异，实际测量时依据可用报表。
- 方法依据：参考摘要中的 Google [英文 AI 指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)、[AI control](https://support.google.com/webmasters/answer/16908024)、[AI report](https://support.google.com/webmasters/answer/16984139)；属于参考记载的官方条件/指标，当前待复核。
- 依赖：官方页面的当前原文、有权限截图/导出；无需全量账户凭据。
- 验证：记录日期、property、实际设置、报告是否可用和指标定义；不将无报表判成无曝光。

### 后续内容队列

| 顺序 | 更新/拟建 | 独立任务 | 所需信息与价值 | 入口与依赖 |
|---|---|---|---|---|
| 1 | 更新 /docs/install | 完成安装和首次运行 | 本次稿件及维护者实测 | 概览已有安装入口；索引技术任务独立处理 |
| 2 | 更新 /docs/troubleshoot | 定位 command not found | 保留同环境、PATH、勿删输入文件；新增原因必须有真实复现 | 安装页原有排错链接 |
| 3 | 复读后再决定更新 /docs/reference | 查询实际参数 | 先取得现有正文，核对 v2 而非假定缺失 | 概览已有入口；受 403 核查依赖 |
| 4 | 更新 /docs | 清楚选择下一篇 | 在确认页面内容后给任务式导航说明 | 现有三入口，不更改 URL |
| 暂不建立 | 无拟建新页 | 尚未证实独立缺口 | 不为 Windows 构造未支持方案，不为同义问法批量建页 | 若未来有真实功能/版本/问题材料，再先检查已有承载页 |

## 4. 安装页完整优化稿

目标页面：https://quartz.example/docs/install。  
选页理由：用户指定，已有事实充分，直接服务完成安装。  
稿件状态：完整英文改稿，命令忠实于站方材料，未经本次运行验证；noindex 与搜索资格另行交接，不妨碍完成文字稿。

### 元数据

- Title: Install Quartz 2 on macOS or Linux | Quartz Docs
- Meta description: Install Quartz 2.0.0 with Python 3.11 or later on macOS or Linux, check the installed version, and format a UTF-8 text file. Windows is not supported.

### 可替换正文开始

# Install Quartz 2

Quartz 2 is a fictional local text formatter. This guide installs version 2.0.0, checks that the command is available, and shows how to format a text file.

## Requirements

You need Python 3.11 or later on macOS or Linux. Quartz 2 does not support Windows.

For the first formatting command below, have a UTF-8 text file named `input.txt` available.

## 1. Install version 2.0.0

Run:

```sh
python -m pip install quartz-demo==2.0.0
```

The Python environment used by this command must meet the Python 3.11-or-later requirement.

## 2. Check the installation

Run:

```sh
quartz-demo --version
```

The expected output is:

```text
2.0.0
```

If `quartz-demo` is not found, check that you are using the same Python environment in which you installed Quartz 2. Then check whether that environment's executable directory is on `PATH`. See [troubleshooting](https://quartz.example/docs/troubleshoot) for these checks. Do not delete input files to fix installation errors.

## 3. Format a text file

Run:

```sh
quartz-demo format input.txt
```

The command prints formatted text to standard output. It does not overwrite `input.txt`.

After checking the version, use this command with your UTF-8 input file to try the formatter. You can return to the [Quartz 2 documentation](https://quartz.example/docs) for the documentation navigation.

### 可替换正文结束

### 编辑说明、内链与事实记录

正文仅使用可读材料中已有命令；没有增加新安装渠道、sudo、Windows 变通法、额外依赖、耗时、性能、示例格式化输出或已实测声称。将排错页中的“同一环境”和“不要删除输入文件”并入相关步骤；它们来自已有明确材料。要求准备 input.txt 是执行所给命令的必要上下文，不声称软件会自动创建它。

正文链接到已读概览与排错。reference 虽在导航中存在，但内容未知，本次不把它描述为包含某个具体参数或指南，也不生成假 URL。未来拿到其正文后再安排有依据的深链。无图片素材与视觉描述。

| 重要事实 | 原始来源 | 状态/阅读日期 | 正文处理 |
|---|---|---|---|
| 本地文本格式化工具、文档 v2 | https://quartz.example/docs | 站方提供的虚构产品材料；2026-10-15 | 保留；未当作真实软件测试结论 |
| Python 3.11+；macOS/Linux；不支持 Windows | https://quartz.example/docs/install | 站方文档；同日 | Requirements 明示 |
| 安装包 quartz-demo==2.0.0 | 同上 | 站方命令；未执行 | 原样保留 |
| --version 输出 2.0.0 | 同上 | 预期输出，非本次运行结果 | 标为 expected |
| format input.txt 接受 UTF-8；输出到 stdout、不覆写 | 同上 | 站方行为说明；未实测 | 紧邻命令保留 |
| 同一 Python 环境与 PATH | install 与 https://quartz.example/docs/troubleshoot | 站方排错说明 | 保留具体检查 |
| 不要删输入文件来修安装错误 | troubleshoot | 站方明确限制 | 保留 |

## 5. 待补素材与复查计划

| 缺失材料/问题 | 用途与位置 | 建议证据 | 是否阻断使用 |
|---|---|---|---|
| 支持环境下安装与命令实测 | 确认安装页准确；必要时更新步骤 | Python/系统版本、执行命令和实际输出记录 | 不阻断本次文档稿交付；发布前由维护者确认，当前不可声称实测成功 |
| noindex 是否有意、响应头与 robots | 决定搜索资格处理 | 负责人确认、HTML/headers与有权限诊断 | 阻断索引资格判断；不阻断正文编辑 |
| reference 正文与 403 原因 | 参考职责与链接准确性 | 正常浏览器正文/导出及必要日志 | 阻断该页内容诊断，不阻断安装稿 |
| Google AI inclusion 与实际报表 | AI资格与测量 | property、父级继承、设置与可用报表截图/导出 | 阻断“已参与/已曝光”结论 |
| 格式化前后例子 | 首次运行之后，可帮助理解行为 | 经维护者实际运行的输入与输出，注明 v2 | 否；本次不造输出 |
| 其他安装失败症状 | 未来扩充排错 | 实际错误文本、环境、可复现步骤 | 否；不补未经证实的通用修复 |

| 复查对象 | 基线/可用数据 | 方法与指标 | 建议窗口与限制 |
|---|---|---|---|
| 文稿与任务完成 | 本次原文；无用户测试 | 命令逐字比对、版本/限制/链接检查；维护者支持环境实测；如有真实读者，观察能否完成步骤 | 发布前与发布后立即；本次没有执行或发布 |
| 索引与控制 | 已见 noindex，其他未知 | 对本 URL 核查相关指令、实际可抓取性、URL Inspection与canonical | 意图确认和部署后再查；指令变化不保证收录 |
| Google 自然搜索 | 无数据 | 取得本页按页面/查询/地区/设备的曝光、点击、CTR | 可从前后各28天可比窗口开始，低量延长；结合其他改动，不证明因果 |
| Google AI | 无后台 | 先核实 inclusion；参考摘要中的 Generative AI performance report 主要看实际可用 AI 曝光维度 | 若是 Web 总体子集，不与总体相加；不可见或导出零值需按帮助文档解释 |
| Bing/Copilot AI | 无后台 | 如实际可用，记录AI Performance引用次数、被引页、grounding queries | 不当作排名、原始用户问题或安装完成率 |
| ChatGPT/Perplexity | 无测试 | 获授权后有限重复任务采样，记模式/日期/地区/语言/原问题/次数/链接/准确性 | 本次未执行；不把一次未引推断为不可发现 |
| 安装完成 | 无分析与业务记录 | 未来以真实可记录的安装验证反馈/任务观察评估；访问量只能作辅助 | 没有数据不编造完成率；AI 引用不等于用户安装 |

## 6. AI 可见性与技术交接

### 现阶段能回答什么

本次材料说明三页正文能被该读取方式取得，安装页带有 noindex，参考页对该工具返回 403。它没有证明任何 AI 产品已抓取、索引、引用或推荐这些文档。也不能从普通访问成功推断 Google Search AI inclusion 已开启。

按技能参考摘要记载，Google AI 功能要求页面已索引、可显示摘要，且对应 Search generative AI control 允许参与；默认 Include 与父级继承规则不能替代本站账户检查。noindex 在被相关爬虫读取并按规则处理时影响索引，因此是需要先核实的明确依赖。摘要、robots、AI设置和实际索引尚不完整，不能宣布“AI 能看到”或“全部 AI 看不到”。

ChatGPT Search 的 OAI-SearchBot、潜在训练的 GPTBot 与用户触发的 ChatGPT-User 是不同用途；本材料未提供其设置。Perplexity 也有独立的搜索与用户触发访问说明。不得为了优化文档就自动开放训练或权限。Bing 对控制指令的解释需按其当前官方原文复核，不把 Google 规则无差别套用。

### 历史中文摘录与较新参考的差异

| 来源与日期 | 材料说了什么 | 本次处理 |
|---|---|---|
| 团队笔记摘录的 Google 中文 AI 功能页，2025-12-31 | “无需额外优化，AI 数据计入 Web 报告” | 是历史摘录，未提供当前完整原文；不能据此宣布没有独立控制或专项报告 |
| 技能参考记载的英文 AI 指南，页面更新 2026-07-10 | 记载索引、摘要、参与控制等资格 | 参考比旧摘录更新且更直接，但本次未联网，状态为离线方法摘要、当前待复核 |
| 技能参考中的 AI control 与 AI performance 帮助页 | 记载自 2026-08-31 推出，并有继承/报告细则 | 作为当前核查路径，不冒充本次已核验，也不推断本站实际设置 |

“继续采用有用内容、不需要特殊AI页面”与“仍有资格和控制条件”可以同时成立；“AI计入Web总体”与“另有子集专项报告”也可以同时成立。需要维护者打开当前具体功能原文核对更新和账户可用性，而不是仅凭语言或一句摘录选边。

| 受影响对象 | 观察证据与日期 | 可确定影响 | 最小建议与未知 |
|---|---|---|---|
| /docs/install | meta noindex；材料2026-10-15 | 存在索引控制；与公开搜索目标可能冲突 | 确认意图、headers/robots/渲染及实际索引；不擅自移除 |
| /docs/reference | 本工具 HTTP 403；同日 | 本次没有正文可分析 | 对具体客户端和日志核查；不声明机器人被挡，不默认放开权限 |
| 对应 Search Console property | 无权限 | 无法确认索引与AI参与状态 | 有权限人员查当前设置及父级继承，保留证据 |
| 抓取/训练控制 | 未取得 robots 或真实日志 | 无法评价 | 如需平台可达判断，按目标平台取最少必要证据；不先列通用技术整改 |

## 附录 A：首次整站 SEO 覆盖状态

已检查指审阅对应材料，不代表通过。以下范围是三个已读正文与一个读取失败，不扩展到未知页面。

| 主题 | 状态 | 结果或限制 |
|---|---|---|
| 工作原理：发现/读取/索引 | 已检查 | 已区分导航发现、正文读取、实际索引 |
| 多久见效 | 已检查 | 建议可比窗口，无排名时效保证 |
| 帮助发现内容 | 已检查 | 现有导航四入口，未取得 sitemap |
| 向用户与Google呈现相同页 | 未验证 | 403仅为工具结果，未测其他客户端/渲染 |
| 排除搜索 | 已检查 | 安装页 noindex；其他标记/响应头未知 |
| 整理网站 | 已检查 | 四类任务分工，参考页待核实 |
| 描述性网址 | 已检查 | /docs/install 等可理解，无迁移理由 |
| 相似主题归组 | 已检查 | 安装与排错合理互链，不按相似判竞争 |
| 减少重复 | 未验证 | 参考正文未知；可读三页无明显相同职责，不能定全站重复率 |
| 实用/可靠/时效/经验 | 已检查 | 版本与限制明确；无运行记录，不造实测 |
| 读者用词 | 已检查 | 用安装/首次运行/排错任务，查询强度未知 |
| 广告干扰 | 未验证 | 未提供视觉页面 |
| 相关资源 | 已检查 | 安装到排错已有关联，reference内容不臆测 |
| 锚文本 | 已检查 | 用 troubleshooting 与 Quartz 2 documentation 指明已有目标 |
| 付费/UGC链接 | 未验证 | 无此场景或 rel 证据 |
| 标题链接 | 已检查 | Install太泛，提供具体版本/系统候选 |
| 摘要 | 已检查 | 新稿描述事实；未提供原description，不声称缺失 |
| 图片/邻近文字 | 未验证 | 未看图 |
| alt | 未验证 | 无图像及用途依据 |
| 视频 | 未验证 | 材料未展示，不能判不存在 |
| 推广 | 未验证 | 无已知渠道，不自动宣传 |
| Search Console | 未验证 | 无账户数据 |
| 长期维护 | 已检查 | 版本、命令、预期输出随产品变化复核 |
| 结构化数据 | 未验证 | 无实现/类型证据；没有 schema任务依据 |
| 官方更新/提问 | 已检查 | 记录新旧来源差异及离线限制 |

| 防误用主题 | 状态 | 本次处理 |
|---|---|---|
| meta keywords | 已检查 | 不加任务 |
| 关键词密度/堆砌 | 已检查 | 无密度或重复词要求 |
| 域名/路径/TLD | 已检查 | 不改路径追求排名 |
| 字数 | 已检查 | 按完成安装需要写，无硬门槛 |
| 子域/目录 | 不适用 | 无迁移目标或证据 |
| PageRank | 未验证 | 无数据，不用链接数替代效果 |
| 重复内容处罚 | 已检查 | 不声称处罚 |
| 标题数量/顺序 | 已检查 | 顺序为执行任务服务 |
| E-E-A-T直接排名因素 | 已检查 | 不评分或造专家，实测状态明示 |

## 附录 B：方法来源与真实日期状态

以下官方直链来自技能参考。参考标注核验日为 2026-10-15；报告在同日离线阅读参考。除表内注明，页面更新日未提供；本次没有新核验官方网页。动态平台结论应在实施时复核。

| 官方来源 | 适用依据与类别 | 参考记录与限制 |
|---|---|---|
| [Google SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide?hl=zh-cn) | 基础覆盖；官方建议 | 参考记更新2025-12-18；本次离线 |
| [Google technical requirements](https://developers.google.com/search/docs/essentials/technical?hl=zh-cn)、[noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing?hl=zh-cn)、[robots](https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=en) | 读取/索引与控制；官方条件 | 当前待复核，不以工具403代替爬虫证据 |
| [People-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content?hl=zh-cn)、[title links](https://developers.google.com/search/docs/appearance/title-link?hl=zh-cn)、[snippets](https://developers.google.com/search/docs/appearance/snippet?hl=zh-cn) | 实用内容与元数据；官方建议 | 不承诺展示原样采用 |
| [Google AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | AI资格与内容建议 | 参考记英文页更新2026-07-10；本次未刷新 |
| [Google AI control](https://support.google.com/webmasters/answer/16908024)、[AI performance report](https://support.google.com/webmasters/answer/16984139) | 参与控制与曝光口径；官方条件/指标 | 参考称2026-08-31推出，本站账户未知 |
| [Google旧中文AI页](https://developers.google.com/search/docs/appearance/ai-features?hl=zh-CN) | 历史说明对照 | 参考/团队笔记记2025-12-31；不作当前唯一规则 |
| [OpenAI bots](https://developers.openai.com/api/docs/bots)、[Perplexity crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) | 各平台搜索/训练/用户访问用途 | 本次仅离线摘要，未取得本站对应设置 |
| [Bing AI Performance announcement](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/)、[Bing guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a?region=france) | 内容建议、引用指标与控制边界 | 参考记公告2026-02-10；指南参考自身仅有搜索索引正文，具体指令效果待正式复核 |
| [Google Search performance](https://support.google.com/webmasters/answer/7576553) | 搜索表现测量 | 无后台实读或导出 |

内容地图、安装步骤编排、优先顺序和28天起始窗口属于工作约定/本站假设，不是强制排名条件。报告不提出 llms.txt、FAQ schema、隐藏AI答案或特殊AI页面作为门槛，不保证收录、排名、引用或安装完成率；没有自动监控、发布或权限修改。
