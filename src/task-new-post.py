import sys
from ualfred import Workflow
from api.task import create_task
import asyncio
from utils.sync import sync

async def main(wf):
    query = " ".join(wf.args)
    if "|" in query:
        task_name, due_date = query.split("|")
    else:
        task_name, due_date = query, None

    token = wf.stored_data('access_token')
    r = await create_task(token, task_name, due_date)
    if r.status_code != 200:
        print("Task could not be created. Please try again.")
    else:
        # await sync(wf, should_fetch_lists=False, should_fetch_tasks=True)
        print('{} task created.'.format(task_name))


if __name__ == u"__main__":
    wf = Workflow()
    asyncio.run(main(wf))
    sys.exit()


