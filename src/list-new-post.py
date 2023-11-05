import sys
from ualfred import Workflow
from api.list import create_list
import asyncio
from utils.sync import sync

async def main(wf):
    list_name = " ".join(wf.args)
    token = wf.stored_data('access_token')
    r = await create_list(token, list_name)
    if r.status_code != 200:
        print("List could not be created. Please try again.")
    else:
        await sync(wf, should_fetch_lists=True, should_fetch_tasks=False)
        print('{} list created.'.format(list_name))


if __name__ == u"__main__":
    wf = Workflow()
    asyncio.run(main(wf))
    sys.exit()


