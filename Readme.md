# Argo Demo

使用 argo 串联 nebula 测试任务。

demo 实现：

1. 在 PR 中触发执行 tck 测试任务。PR 评论 /test
2. GitHub 触发 webhook
3. HTTP server 接收 webhook，然后调用 argo api，生成 argo workflow。
4. HTTP server 查询 workflow 结果状态，将结果贴在 GitHub PR。
