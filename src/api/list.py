from lib.constants import TICKTICK_API_URL, HEADERS
from ualfred import web

def get_lists():
    url = TICKTICK_API_URL + '/project'
    return web.get(url, headers=HEADERS).json()
