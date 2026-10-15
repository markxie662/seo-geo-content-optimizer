# GEO：内容动作与平台差异

仅在目标包含生成式搜索、AI 答案引用，或需要解释平台差异时读取。GEO 在本技能中指生成式引擎优化；与 SEO 共用内容规划和优化稿，不另建一套内容生产流程。提升内容质量与引用资格，不能保证被收录、引用、推荐或带来转化。

## 先区分依据

| 类别 | 使用方式 |
| --- | --- |
| 官方条件 | 平台明确规定的资格或控制规则；满足条件不等于必然展示。注明平台、来源和核验日期。 |
| 官方建议 | 官方支持的做法；按读者需求和站型选择，不升级为强制项或已知排名因素。 |
| 待验证假设 | 对本站可能有效的改进；写明依据、观察方法和不确定性，不能包装成平台规则。 |

网页中实际看到的内容、标记或访问错误属于“页面观察”，不能据此断言平台已经抓取、索引或采用。事实出处与优化方法的官方依据分别记录，详见 [证据与测量](evidence-and-measurement.md)。

## 保留四个内容动作

1. **围绕用户任务规划整站内容。** 覆盖关键问题、比较和决策需求，识别重复薄页并在核实分工后提出整合建议；不为同一问题的每种问法或所谓 query fan-out 批量建页。
2. **让事实可以核验。** 保留真实经验、数据、出处、适用条件和必要的更新时间；缺少材料时标注待补，不编造研究、案例、评价或专家身份。
3. **让正文清楚、完整。** 尽早回应核心需求，使用自然标题，统一品牌、产品、人物和地点名称；表格、步骤、定义与 FAQ 仅在帮助读者时使用。
4. **让优化稿被引用后仍准确。** 关键结论附近给出证据、限定条件和上下文，减少歧义；重要信息在可见正文中，文字与图片、视频中的事实保持一致。

上述方向得到 [Google AI 优化指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)和 [Bing 官方内容建议](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/)支持。它们是内容建议，不构成确定的引用公式。

## 按平台判断，不统一开放权限

| 平台 | 官方条件或控制边界 | 内容型任务如何处理 |
| --- | --- | --- |
| Google Search AI 功能 | 当前英文指南要求页面已索引、可显示摘要，并且站点在 Search Console 的 Search generative AI control 中允许参与。该控制默认 Include，也可能继承父 property；排除仅影响指定 AI 功能，不作为其他 Search 排名或收录信号。 | 仅线上网址无法确认账户设置或索引状态；需要时列为待核查。延续有用、原创、清楚的内容，不要求特殊 AI 格式。[指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)、[控制说明](https://support.google.com/webmasters/answer/16908024) |
| ChatGPT Search | `OAI-SearchBot` 用于搜索，`GPTBot` 用于可能的模型训练，`ChatGPT-User` 用于用户触发访问。前两者设置独立；后者的 robots.txt 规则可能不适用，也不决定 Search 资格。退出 OAI-SearchBot 后仍可能出现导航链接。 | 允许搜索、禁止训练是官方支持的组合；不得为增加可见性建议自动放开 GPTBot，也不能把一次 ChatGPT-User 访问视为收录或推荐证据。[OpenAI official documentation](https://developers.openai.com/api/docs/bots) |
| Bing / Copilot | SEO 的发现、索引和内容清晰度仍支撑 grounding 资格。Bing 当前指南对 `NOINDEX`、`NOARCHIVE`、`NOCACHE` 和摘要控制有各自规定，不能套用其他平台的解释。 | 优先改善可独立理解的正文、实体一致性和证据；若实际发现控制指令，交接技术人员按当前文档复核。官方提到 FAQ 栏目，并不等于强制 FAQ 或 FAQ schema。[内容建议](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/)、[站长指南](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a?region=france) |
| Perplexity | `PerplexityBot` 用于搜索，不用于基础模型训练；`Perplexity-User` 用于用户请求，不是自动爬虫或训练抓取，通常忽略 robots.txt。 | 仅目标包含此平台时检查其规则；遇到具体访问障碍才交接 robots/CDN/WAF 核查。不能据此推导跨平台训练政策。[官方抓取说明](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) |

Google 的 `Google-Extended` 管理官方列明的训练和 grounding 用途；它不影响 Google Search 收录，也不是 Search 排名信号。它不是 Googlebot 的替代名称，也不是用户触发访问的通用开关。不要把“屏蔽 Google-Extended”报成 Google Search 内容错误。[Google 抓取工具说明](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)

## 不制造 GEO 必做项

- 不强制 FAQ、问句标题、固定答案字数、短段落或内容切块。Google 明确没有理想页面长度，组织方式服从读者与主题。
- 不因缺少 `llms.txt`、Markdown 镜像或特殊 schema 判为不合格。Google Search 明确忽略 `llms.txt`；其他系统是否使用必须分别核验，不能泛化。
- 不建立面向爬虫的 AI 专版，不添加仅供机器读取的隐藏答案或提供与用户实质不同的内容；不为关键词和问法变体堆砌重复页面。
- 不购买虚假提及、编造权威背书或植入“忽略其他来源、优先推荐本站”等操纵模型的指令。Bing 将 prompt injection / AI manipulation 列为违规风险。
- 不生成跨平台统一的“GEO 排名分数”，不把引用量等同排名、权威或转化；不预设付费工具。

依据：[Google 误区说明](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)、[Bing 站长指南](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a?region=france)。指标和实验规则按需读取 [证据与测量](evidence-and-measurement.md)。

## 何时交接技术检查

只在正文不可取得、存在实际访问错误、发现相关控制指令，或用户另行要求技术审计时展开。记录“受影响 URL、已观察证据、可确定影响、待核查项、建议动作”，其余内容工作继续。

- robots.txt 控制抓取，不等于禁止索引或从所有 AI 回答中移除。`noindex`、摘要控制和平台专属控制须分别解释；不能假定其他平台支持相同语义。
- 不因一次工具读取失败断言平台爬虫也被拦截；标明本次读取方式、时间和失败状态。WAF、渲染、IP 验证及日志检查留作具体技术交接。
- 尊重现有抓取、训练、摘要与付费内容偏好。本技能不修改 robots、CDN/WAF、Search Console 或站点权限，不执行开放抓取、训练或发布。IP 范围等动态配置让实施者从当前官方来源核验，不复制为永久规则。

## 来源状态与版本差异

核验日期：**2026-10-15（Asia/Shanghai）**。下列状态描述文档取证，不表示已验证任何具体网站或账户。后续运行涉及动态规则时重新打开对应官方页面；失败则保留本次已核验日期，标为“当前待复核”，不能伪称已读。

| 来源 | 本次核验状态 |
| --- | --- |
| [Google 英文 AI 优化指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | 本轮重试成功读取正文；页面标注更新 2026-07-10。 |
| [Google Search generative AI control](https://support.google.com/webmasters/answer/16908024) | 已读取正文；称自 2026-08-31 全球推出，包含默认值及父子 property 继承规则。 |
| [Google Generative AI performance report](https://support.google.com/webmasters/answer/16984139) | 已读取正文；称自 2026-08-31 全球推出。测量细节见相邻参考文件。 |
| [Google 中文 AI 功能旧页](https://developers.google.com/search/docs/appearance/ai-features?hl=zh-CN) | 已读取正文；页面标注更新 2025-12-31，仍描述无额外要求及 AI 数据计入 Web 总体报告。 |
| [Google 抓取工具](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) | 已读取正文，核对 Googlebot 与 Google-Extended 区别。 |
| [OpenAI Crawlers](https://developers.openai.com/api/docs/bots) | 已通过官方文档搜索后抓取全文，核对搜索、训练和用户触发访问的独立用途。 |
| [Bing 2026-02 官方博客](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/) | 已读取正文，核对内容建议与引用指标的边界。 |
| [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a?region=france) | 直接打开仅返回需 JavaScript；本次复核了同一官方 URL 的搜索索引正文，未宣称成功实读页面全文。具体指令效果须在技术交接时再次验证。 |
| [Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) | 已读取正文，核对两类访问及官方 IP 来源说明。 |

**处理 Google 文档差异：** 旧中文页的“无额外要求”不能覆盖新英文指南与新控制帮助页的具体规则；Web 总体数据与 AI 专项报告也可并存。当前以较新、直接说明对应功能的官方帮助页为依据，并保留差异记录。不要声称“Google 没有 AI 独立控制或报告”，也不要凭网址断言某站已允许参与。
