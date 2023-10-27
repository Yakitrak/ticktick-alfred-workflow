import sys
from ualfred import Workflow, ICON_WARNING
from api.task import get_all_tasks
from utils.filters import key_for_task

def main(wf):
    query = wf.args[0] if len(wf.args) else None
    token = wf.stored_data('token')
    tasks = wf.cached_data('tasks', lambda: get_all_tasks(token), max_age=60)

    items = wf.filter(query, tasks, key_for_task) if query else tasks

    if not items:
        wf.add_item('No tasks match your query', icon=ICON_WARNING)

    for item in items:
        wf.add_item(item['title'], subtitle=item['id'], arg=item['id'], valid=True)


    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))


