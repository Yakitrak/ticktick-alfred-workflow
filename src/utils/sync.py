from api.list import get_lists
from api.task import get_all_tasks
from utils.constants import CACHE_AGE


async def sync(wf, should_fetch_lists=False, should_fetch_tasks=False):
    token = wf.stored_data('access_token')
    if should_fetch_lists:
        wf.cached_data('lists', None)
        wf.cached_data('lists', lambda: get_lists(token), max_age=CACHE_AGE)
    if should_fetch_tasks:
        wf.cached_data('tasks', None)
        tasks = await get_all_tasks(token)
        wf.cache_data('tasks', tasks)
