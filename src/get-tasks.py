import sys
from ualfred import Workflow, ICON_WARNING
from api.task import get_all_tasks
from utils.filters import is_today, is_tomorrow, key_for_task
from utils.displays import generate_task_display
import asyncio


async def main(wf):
    query = wf.args[0] if len(wf.args) else None
    token = wf.stored_data('access_token')

    # get_all_tasks is an async function, so we need to use asyncio.run to run it
    cached_tasks = wf.cached_data('tasks', max_age=60)
    if cached_tasks is None:
        tasks = await get_all_tasks(token)
        wf.cache_data('tasks', tasks)
    else:
        tasks = cached_tasks

    # filter tasks based on query
    if query is None:
        items = tasks
    elif query == '@today' or query == '@tod':
        items = list(filter(is_today, tasks))
    elif query == '@tomorrow' or query == '@tom':
        items = list(filter(is_tomorrow, tasks))
    else:
        items = wf.filter(query, tasks, key_for_task)

    if not items:
        wf.add_item('No tasks match your query', icon=ICON_WARNING)

    for item in items:
        title, subtitle = generate_task_display(item)
        arg = '{}/tasks/{}'.format(item['list_id'], item['id'])
        wf.add_item(title=title, subtitle=subtitle, arg=arg, valid=True)

    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    asyncio.run(main(wf))
    sys.exit()


