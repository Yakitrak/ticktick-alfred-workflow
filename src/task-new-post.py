import sys
from ualfred import Workflow
from api.task import create_task
from utils.parse import parse_new_task

def main(wf):
    query = " ".join(wf.args)
    if "|" in query:
        task_name, due_date = query.split("|")
    else:
        task_name, due_date = query, None

    token = wf.stored_data('access_token')
    r = create_task(token, task_name, due_date)
    if r.status_code != 200:
        print("Task could not be created. Please try again.")
    else:
        # wf.clear_cache() # uncomment when tasks can be retrieved from inbox
        print('{} task created.'.format(task_name))


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))

