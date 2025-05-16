# KeepAliveE5

通过 GitHub Actions 定期调用 Microsoft Graph API，保持 E5 开发者账号活跃。

## 配置步骤

1. Fork 本项目到你的 GitHub 账号
2. 在仓库设置中添加以下 Secrets：
   - `CLIENT_ID`
   - `CLIENT_SECRET`
   - `TENANT_ID`
3. 手动运行一次 Workflow，确保调用成功
4. 系统将每 6 小时自动运行一次，保持账号活跃

## 注意事项

- 请确保 Azure 应用已授权 Microsoft Graph API 权限
- 若调用失败，请检查密钥是否正确
