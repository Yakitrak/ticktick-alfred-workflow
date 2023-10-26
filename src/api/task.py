from .list import get_lists
from utils.constants import TICKTICK_API_URL
from ualfred import web


def get_tasks_from_list(list_id, token):
    headers = { "Authorization": "Bearer " + token }
    url = TICKTICK_API_URL + '/project/' + list_id + '/data'
    return web.get(url, headers=headers).json()


def get_all_tasks(token):
    lists = get_lists(token)
    list_ids = [l['id'] for l in lists]

    tasks = []
    for list_id in list_ids:
        tasks.extend(get_tasks_from_list(list_id, token)['tasks'])

    return tasks


