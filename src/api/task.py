from concurrent.futures import ThreadPoolExecutor
from .list import get_lists
from utils.constants import TICKTICK_API_URL
from ualfred import web


def get_tasks_from_list(list_id, token):
    headers = {"Authorization": "Bearer " + token}
    url = TICKTICK_API_URL + '/project/' + list_id + '/data'
    resp = web.get(url, headers=headers).json()
    tasks = []
    list_name = resp['project']['name']
    for task in resp['tasks']:
        task['list_name'] = list_name
        task['list_id'] = list_id
        tasks.append(task)
    return tasks

def get_all_tasks(token):
    lists = get_lists(token)
    list_ids = [l['id'] for l in lists]

    tasks = []
    with ThreadPoolExecutor(5) as executor:
        futures = [executor.submit(get_tasks_from_list, list_id, token) for list_id in list_ids]
        for future in futures:
            result = future.result()
            tasks.extend(result)
    return tasks

def complete_task(path, token):
    headers = {"Authorization": "Bearer " + token}
    url = TICKTICK_API_URL + path
    resp = web.post(url, headers=headers).json()
    return resp
