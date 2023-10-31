import sys
from ualfred import Workflow
from api.task import create_task
from utils.parse import parse_new_task

def main(wf):
    query = " ".join(wf.args)
    task_details = parse_new_task(query)
    task_name = task_details['name']
    due_date = task_details['due_date']

    token = wf.stored_data('access_token')
    r = create_task(token, task_name, due_date)
    if r.status_code != 200:
        print("Task could not be created. Please try again.")
    else:
        wf.clear_cache()
        print('{} task created.'.format(task_name))


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))

