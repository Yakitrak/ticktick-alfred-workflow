import os
import requests
def fetch_access_token(code):
    url = "https://ticktick.com/oauth/token"
    data = {
        "client_id": os.getenv("client_id"),
        "client_secret": os.getenv("client_secret"),
        "code": code,
        "grant_type": "authorization_code",
        "scope": "tasks:write tasks:read",
        "redirect_uri": "http://localhost",
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    r = requests.post(url, data=data, headers=headers).json()
    return r["access_token"]
