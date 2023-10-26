from utils.constants import TICKTICK_API_URL
from ualfred import web

def get_lists(token):
    headers = {
        "Authorization": "Bearer " + token,
    }
    url = TICKTICK_API_URL + '/project'
    return web.get(url, headers=headers).json()
