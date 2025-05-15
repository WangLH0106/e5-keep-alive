
import requests
import os

# Get secrets from environment variables
tenant_id = os.getenv('TENANT_ID')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# Get access token
def get_access_token(tenant_id, client_id, client_secret):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default'
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()['access_token']

# List OneDrive files
def list_onedrive_files(access_token):
    url = "https://graph.microsoft.com/v1.0/me/drive/root/children"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

# Main function
def main():
    access_token = get_access_token(tenant_id, client_id, client_secret)
    files = list_onedrive_files(access_token)
    print("OneDrive files:")
    for file in files['value']:
        print(file['name'])

if __name__ == "__main__":
    main()
