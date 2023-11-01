import sys
from ualfred import Workflow
from api.task import create_task
from utils.parse import parse_new_task

def main(wf):
    query = " ".join(wf.args)
    task_details = parse_new_task(query)
    task_name = task_details['name']
    due_date = task_details['due_date']

    title = "TickTick Task New: {}".format(task_name)
    subtitle = "Create a new task with name '{}' and due date '{}'".format(task_name, due_date)
    arg = " ".join([task_name, due_date])
    wf.add_item(title=title, subtitle=subtitle, arg=arg, valid=True)
    wf.send_feedback()




if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))

