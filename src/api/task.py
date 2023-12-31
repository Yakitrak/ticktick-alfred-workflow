from concurrent.futures import ThreadPoolExecutor
from .list import get_lists
from utils.constants import TICKTICK_API_URL
import requests
import asyncio

session = requests.Session()
async def get_tasks_from_list(token, list_id):
    headers = {"Authorization": "Bearer " + token}
    url = TICKTICK_API_URL + '/project/' + list_id + '/data'
    resp = session.get(url, headers=headers).json()
    tasks = []
    list_name = resp['project']['name']
    for task in resp['tasks']:
        task['list_name'] = list_name
        task['list_id'] = list_id
        tasks.append(task)
    return tasks

async def get_all_tasks(token):
    lists = get_lists(token)
    list_ids = [l['id'] for l in lists]
    tasks = []
    tasks_data = await asyncio.gather(*[get_tasks_from_list(token, list_id) for list_id in list_ids])
    for data in tasks_data:
        tasks.extend(data)
    return tasks

# previous script filter will output "list_id/tasks/task_id" as arg, but we need "list_id/tasks/task_id"
async def complete_task(token, arg):
    path = arg.replace('tasks', 'task')
    headers = {"Authorization": "Bearer " + token}
    url = TICKTICK_API_URL + '/project/' + path + '/complete'
    return requests.post(url, headers=headers)

async def create_task(token, task_name, due_date=None):
    headers = {"Authorization": "Bearer " + token}
    url = TICKTICK_API_URL + '/task'
    data = {
        'title': task_name,
    }
    if due_date:
        data['dueDate'] = due_date
        if due_date.endswith('T00:00:00+0000'):
            data['isAllDay'] = True

    # print(data)
    return requests.post(url, headers=headers, json=data)

