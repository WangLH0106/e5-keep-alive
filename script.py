import os
import requests
from datetime import datetime, timedelta

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
tenant_id = os.getenv('TENANT_ID')

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
        print("❌ 获取 Access Token 失败")
        print("状态码：", response.status_code)
        print("响应内容：", response.text)
        exit(1)

    return response.json().get("access_token")


access_token = get_access_token(client_id, client_secret, tenant_id)

def get_onedrive_files(access_token):
    endpoint = "https://graph.microsoft.com/v1.0/me/drive/root/children"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()['value']

def get_outlook_emails(access_token):
    endpoint = "https://graph.microsoft.com/v1.0/me/mailFolders/Inbox/messages?$top=5"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()['value']

def get_calendar_events(access_token):
    start = datetime.utcnow().isoformat() + 'Z'
    end = (datetime.utcnow() + timedelta(days=7)).isoformat() + 'Z'
    endpoint = f"https://graph.microsoft.com/v1.0/me/calendarView?startDateTime={start}&endDateTime={end}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()['value']

def get_teams_messages(access_token):
    endpoint = "https://graph.microsoft.com/v1.0/me/chats"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()['value']

def upload_file_to_onedrive(access_token, file_name, file_content):
    endpoint = f"https://graph.microsoft.com/v1.0/me/drive/root:/{file_name}:/content"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "text/plain"
    }
    response = requests.put(endpoint, headers=headers, data=file_content)
    response.raise_for_status()
    return response.json()

onedrive_files = get_onedrive_files(access_token)
outlook_emails = get_outlook_emails(access_token)
calendar_events = get_calendar_events(access_token)
teams_messages = get_teams_messages(access_token)
uploaded_file = upload_file_to_onedrive(access_token, "test_file.txt", "This is a test file uploaded by the script.")

with open('README.md', 'w') as f:
    f.write("# Microsoft Graph API - 自动化脚本运行结果\n\n")

    f.write("## OneDrive 文件列表\n")
    for file in onedrive_files:
        f.write(f"- {file['name']} ({'folder' if 'folder' in file else 'file'})\n")

    f.write("\n## Outlook 最近 5 封邮件\n")
    for email in outlook_emails:
        f.write(f"- {email['subject']} (from {email['from']['emailAddress']['address']})\n")

    f.write("\n## 未来 7 天的日历事件\n")
    for event in calendar_events:
        f.write(f"- {event['subject']} (from {event['start']['dateTime']} to {event['end']['dateTime']})\n")

    f.write("\n## 最近的 Teams 聊天消息\n")
    for chat in teams_messages:
        f.write(f"- {chat.get('topic', 'No topic')} (last updated {chat['lastUpdatedDateTime']})\n")

    f.write("\n## 上传的测试文件\n")
    f.write(f"- {uploaded_file['name']} (size: {uploaded_file['size']} bytes)\n")

print("✅ 所有功能执行完毕，结果已写入 README.md")
