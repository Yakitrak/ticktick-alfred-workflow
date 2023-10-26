from .list import get_lists
from utils.constants import TICKTICK_API_URL, HEADERS
from ualfred import web


def get_tasks_from_list(list_id):
    url = TICKTICK_API_URL + '/project/' + list_id + '/data'
    return web.get(url, headers=HEADERS).json()


def get_all_tasks():
    lists = get_lists()
    list_ids = [l['id'] for l in lists]

    tasks = []
    for list_id in list_ids:
        tasks.extend(get_tasks_from_list(list_id)['tasks'])

    return tasks

def get_today_tasks():
    tasks = get_all_tasks()
    today_tasks = []
    for task in tasks:
        if task['dueDate'] == 'Today':
            today_tasks.append(task)
    return today_tasks
