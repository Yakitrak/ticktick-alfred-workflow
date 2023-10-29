import sys
from ualfred import Workflow
import requests
import os

def main(wf):
    url = "https://ticktick.com/oauth/token"
    data = {
        "client_id": os.getenv("client_id"),
        "client_secret": os.getenv("client_secret"),
        "code":  wf.args[0],
        "grant_type": "authorization_code",
        "scope": "tasks:write tasks:read",
        "redirect_uri": "http://localhost",
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    r = requests.post(url, data=data, headers=headers)
    if r.status_code != 200:
        print("TickTick Authorisation failed. Please check your code and try again.")
    else:
        wf.store_data('access_token', r.json()["access_token"])
        print("You are now authenticated to TickTick.")

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))


