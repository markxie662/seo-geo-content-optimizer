# 用户任务
使用 $seo-geo-content-optimizer 分析 https://lanhe.example，给出整站内容规划，并完整改写服务页。目标是帮助采购者理解服务与合作前提。

# 模拟网站读取材料
本离线材料是本次可用的完整读取结果。不要访问网络；官方方法来源可使用技能参考，但不可声称本次新核验。页面读取时间为 2026-10-15 Asia/Shanghai。没有 Search Console、关键词数据库、分析工具或 Bing 后台数据。导航和 sitemap 均发现以下四页，未提供其他发现渠道。它们均为 HTTP 200；以下内容为可读取完整正文。

URL: https://lanhe.example/
<title>岚禾信息设计</title>
<meta name="description" content="把资料整理好，再谈智能。">
# 把资料整理好，再谈智能
岚禾信息设计为中小企业梳理内部知识资料。我们先梳理资料来源和权限，再设计目录、术语与维护责任，最后整理交接说明。
我们的工作是信息梳理与内容设计。我们不代建软件，也不承诺模型回答准确率。
[了解服务](/services) [了解我们](/about) [预约沟通](/contact)

URL: https://lanhe.example/services
<title>服务</title>
# 知识资料整理
适合内部文档来源分散、不同部门术语不一致的中小企业。
交付资料清单、目录与术语建议、维护责任表、交接说明。
开始前需要指定一名内部联系人，确认哪些资料可以提供，以及谁有权决定资料的使用范围。
我们不代建软件，不接收未经授权的资料，也不承诺模型回答准确率。
有需要请[联系岚禾](/contact)。

URL: https://lanhe.example/about
<title>关于岚禾</title>
# 关于岚禾
我们关注信息如何被理解和持续维护。公开页面没有提供成立年份、客户名单、团队履历、奖项或成效数据。
[查看服务](/services)

URL: https://lanhe.example/contact
<title>联系岚禾</title>
# 联系岚禾
请邮件介绍你的资料类型、目前遇到的问题，以及是否已有内部负责人。邮箱 hello@lanhe.example。

GET /robots.txt: 200
User-agent: OAI-SearchBot
Allow: /
User-agent: GPTBot
Disallow: /
User-agent: Google-Extended
Disallow: /
User-agent: *
Allow: /
GET /llms.txt: 404
页面没有 FAQ schema；所有页面 canonical 均为自己的完整 URL。没有取得 Google AI inclusion 后台设置。
