import sys
import json
from ualfred import Workflow
from api.task import create_task, create_task_full
import asyncio


async def main(wf):
    query = " ".join(wf.args)
    token = wf.stored_data('access_token')

    if not token:
        print("Please run 'tsetup' to authenticate with TickTick first.")
        return

    try:
        task_data = json.loads(query)
        task_name = task_data.get('title', 'Task')
        r = await create_task_full(token, task_data)
    except json.JSONDecodeError:
        if "|" in query:
            task_name, due_date = query.split("|")
        else:
            task_name, due_date = query, None

        r = await create_task(token, task_name, due_date)

    if r.status_code != 200:
        print(f"Task could not be created: {r.text}")
    else:
        print(f"'{task_name}' created.")


if __name__ == u"__main__":
    wf = Workflow()
    asyncio.run(main(wf))
    sys.exit()
