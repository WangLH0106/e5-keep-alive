import os
import requests

access_token = os.getenv('ACCESS_TOKEN')
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
