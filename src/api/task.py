from concurrent.futures import ThreadPoolExecutor
from .list import get_lists
from utils.constants import TICKTICK_API_URL
import requests

def get_tasks_from_list(token, list_id):
    headers = {"Authorization": "Bearer " + token}
    url = TICKTICK_API_URL + '/project/' + list_id + '/data'
    resp = requests.get(url, headers=headers).json()
    tasks = []
    list_name = resp['project']['name']
    for task in resp['tasks']:
        task['list_name'] = list_name
        task['list_id'] = list_id
        tasks.append(task)
    return tasks

def get_all_tasks(token):
    print(token)
    lists = get_lists(token)
    list_ids = [l['id'] for l in lists]
    tasks = []
    with ThreadPoolExecutor(5) as executor:
        futures = [executor.submit(get_tasks_from_list, token, list_id) for list_id in list_ids]
        for future in futures:
            result = future.result()
            tasks.extend(result)
    return tasks

# previous script filter will output "list_id/tasks/task_id" as arg, but we need "list_id/tasks/task_id"
def complete_task(token, arg):
    path = arg.replace('tasks', 'task')
    headers = {"Authorization": "Bearer " + token}
    url = TICKTICK_API_URL + '/project/' + path + '/complete'
    return requests.post(url, headers=headers)

def create_task(token, task_name, due_date=None):
    headers = {"Authorization": "Bearer " + token}
