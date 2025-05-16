import os
import requests

# 从环境变量中读取
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
tenant_id = os.getenv('TENANT_ID')

# 打印调试信息（不打印值，只打印是否为空）
print(f"CLIENT_ID is {'set' if client_id else 'NOT set'}")
print(f"CLIENT_SECRET is {'set' if client_secret else 'NOT set'}")
print(f"TENANT_ID is {'set' if tenant_id else 'NOT set'}")

# 获取 Access Token
def get_access_token(client_id, client_secret, tenant_id):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://graph.microsoft.com/.default"
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 200:
        print("Failed to get access token:")
        print(response.status_code)
        print(response.text)
        exit(1)
    return response.json().get("access_token")

access_token = get_access_token(client_id, client_secret, tenant_id)

# 调用 OneDrive API
endpoint = "https://graph.microsoft.com/v1.0/me/drive/root/children"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

response = requests.get(endpoint, headers=headers)

if response.status_code == 200:
    files = response.json()
    print("Files in OneDrive:")
    for file in files['value']:
        print(f"Name: {file['name']}, Type: {'folder' if 'folder' in file else 'file'}")
else:
    print(f"Error: {response.status_code}")
    print(response.json())
