import os
import requests

def get_access_token():
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    tenant_id = os.getenv("TENANT_ID")

    if not all([client_id, client_secret, tenant_id]):
        print("❌ 缺少必要的环境变量 CLIENT_ID、CLIENT_SECRET 或 TENANT_ID")
        return None

    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    body = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://graph.microsoft.com/.default"
    }

    response = requests.post(token_url, headers=headers, data=body)
    if response.status_code != 200:
        print("❌ 获取 access token 失败:", response.status_code, response.text)
        return None

    token = response.json().get("access_token")
    print("✅ 成功获取 access token")
    return token

def call_graph_api(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = "https://graph.microsoft.com/v1.0/me"
    response = requests.get(url, headers=headers)

    print("📡 Graph API 响应状态码:", response.status_code)
    try:
        print("📄 响应内容:", response.json())
    except Exception as e:
        print("⚠️ 无法解析响应:", e)

if __name__ == "__main__":
    token = get_access_token()
    if token:
        call_graph_api(token)
