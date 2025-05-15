# Microsoft Graph API - OneDrive 活跃脚本

本项目通过 GitHub Actions 每天调用一次 Microsoft Graph API，获取 OneDrive 文件列表，以保持 Microsoft 365 E5 开发者账号活跃。

## 🧾 步骤一：注册 Azure 应用

1. 登录 Azure Portal
2. 进入 **Azure Active Directory > 应用注册 > 新注册**
3. 填写名称，注册应用
4. 记录 **Client ID** 和 **Tenant ID**
5. 添加权限：Microsoft Graph > `Files.Read`
6. 创建 **Client Secret**，记录 Secret 值

## 🔐 步骤二：获取 Access Token

你可以使用 Postman、脚本，或 Microsoft 提供的 Graph Explorer 获取 Access Token。

## 🔧 步骤三：配置 GitHub Secrets

在你的 GitHub 仓库中添加以下 Secrets：

- `ACCESS_TOKEN`：你获取的 Microsoft Graph API 访问令牌

## 🏃 步骤四：运行工作流

GitHub Actions 会每天运行一次 `script.py`，也可以手动运行：

1. 打开 GitHub 仓库 → 点击 **Actions**
2. 选择工作流 → 点击 **Run workflow**
