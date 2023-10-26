import sys
from ualfred import Workflow
from ualfred.notify import notify
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
    r = requests.post(url, data=data, headers=headers).json()
    wf.store_data('token', r["access_token"])
    notify('Setup completed', 'You can now use TickTick Alfred workflow')

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))


