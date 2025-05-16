import requests
import os

def keep_alive():
    token = os.getenv("ACCESS_TOKEN")
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = "https://graph.microsoft.com/v1.0/me"
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    print("Response:", response.json())

if __name__ == "__main__":
    keep_alive()
