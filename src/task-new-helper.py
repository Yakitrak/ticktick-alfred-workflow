import sys
from ualfred import Workflow
from utils.parse import parse_new_task

def main(wf):
    query = " ".join(wf.args)

    if query.count(',') > 1:
        wf.add_item(title="Too many commas", subtitle="Please only use one comma to separate your task name and due date", valid=True)
        wf.send_feedback()
        return

    task_name, task_due_formatted, task_due_pretty = parse_new_task(query)

    title = "TickTick Task New: {}".format(task_name)
    subtitle = "Create a new task with name '{}'".format(task_name)
    arg = "{}|{}".format(task_name, task_due_formatted) if task_due_formatted else task_name

    if task_due_pretty:
        subtitle += " and due {}".format(task_due_pretty)
    else:
        subtitle += " (try using a comma and then add your time, e.g. tomorrow 10am)"

    wf.add_item(title=title, subtitle=subtitle, arg=arg, valid=True)
    wf.send_feedback()




if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))

