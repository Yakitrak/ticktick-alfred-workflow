import sys
from ualfred import Workflow
from utils.sync import sync
import asyncio

async def main(wf):
    wf.logger.debug("Starting sync")
    await sync(wf, should_fetch_lists=True, should_fetch_tasks=True)
    wf.logger.debug("Finished sync")
    print("Sync complete")


if __name__ == u"__main__":
    wf = Workflow()
    asyncio.run(main(wf))
    sys.exit()
