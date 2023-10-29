import sys
from ualfred import Workflow
from api.task import complete_task

def main(wf):
    query = wf.args[0] if len(wf.args) else None
    token = wf.stored_data('access_token')
    completed_task = complete_task(token, query)
    # notify


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))

