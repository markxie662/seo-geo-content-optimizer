# 用户任务
使用 $seo-geo-content 为 https://quartz.example/docs 做内容规划，完整改写安装页。我最希望读者完成安装；也想知道 AI 搜索是否能看到文档。所有输出正文用英语，报告说明用中文。

# 模拟网站读取材料
仅使用离线材料，不访问网络。读取时间 2026-10-15 Asia/Shanghai。导航发现 /docs、/docs/install、/docs/reference、/docs/troubleshoot。没有后台权限或报告。reference 页面本次读取返回 HTTP 403，正文未知；其余完整正文如下。不存在额外已读页面。

URL: https://quartz.example/docs
HTTP: 200
<title>Quartz Docs</title>
# Quartz 2 documentation
Quartz is a fictional local text formatter. This documentation covers version 2. The navigation links to install, reference and troubleshooting.

URL: https://quartz.example/docs/install
HTTP: 200
<meta name="robots" content="noindex">
<title>Install</title>
# Install Quartz 2
Requirements: Python 3.11 or later. Supported systems: macOS and Linux.
Install with: python -m pip install quartz-demo==2.0.0
Check the installation with: quartz-demo --version
Expected output: 2.0.0
Then format a UTF-8 text file with: quartz-demo format input.txt
The command prints formatted text to standard output and does not overwrite input.txt.
If quartz-demo is not found, check that the environment's executable directory is on PATH. More information: [troubleshooting](/docs/troubleshoot).
Quartz 2 does not support Windows. No installation duration or performance measurements are supplied.

URL: https://quartz.example/docs/troubleshoot
HTTP: 200
<title>Troubleshooting</title>
# Command not found
Make sure you are using the same Python environment in which Quartz 2 was installed. Check whether that environment's executable directory is on PATH. Do not delete input files to fix installation errors.

URL: https://quartz.example/docs/reference
HTTP: 403 returned to this reading tool. No other client or crawler test was performed.

附带历史资料：一份团队笔记摘录了 2025-12-31 的 Google 简中 AI 功能说明：“无需额外优化，AI 数据计入 Web 报告”。团队尚未查阅更新文档或账户设置。
