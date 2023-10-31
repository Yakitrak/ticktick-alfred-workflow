import sys
from ualfred import Workflow
from api.task import complete_task

def main(wf):
    query = wf.args[0] if len(wf.args) else None
    token = wf.stored_data('access_token')
    r = complete_task(token, query)
    if r.status_code != 200:
        print("Task completion failed. Please try again.")
    else:
        wf.clear_cache()
        print("Task completed.")


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))

