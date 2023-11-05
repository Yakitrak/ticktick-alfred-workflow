import sys
from ualfred import Workflow
from api.task import complete_task
from utils.sync import sync
import asyncio

async def main(wf):
    query = wf.args[0] if len(wf.args) else None
    token = wf.stored_data('access_token')
    r = await complete_task(token, query)
    if r.status_code != 200:
        print("Task completion failed. Please try again.")
    else:
        await sync(wf, should_fetch_lists=False, should_fetch_tasks=True)
        print("Task completed.")


if __name__ == u"__main__":
    wf = Workflow()
    asyncio.run(main(wf))
    sys.exit()

