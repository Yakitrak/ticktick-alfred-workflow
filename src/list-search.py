import sys
from ualfred import Workflow, ICON_WARNING
from api.list import get_lists
from utils.filters import key_for_list

def main(wf):
    query = wf.args[0] if len(wf.args) else None
    token = wf.stored_data('access_token')
    lists = wf.cached_data('lists', lambda: get_lists(token), max_age=60)

    inbox_item = {
        'id': 'inbox',
        'name': 'Inbox',
        'kind': 'Task'
    }

    lists.insert(0, inbox_item)
    items = wf.filter(query, lists, key_for_list) if query else lists

    if not items:
        wf.add_item('No lists match your query', icon=ICON_WARNING)

    for item in items:
        subtitle = item['kind'].title() + ' List'
        wf.add_item(item['name'], subtitle=subtitle, arg=item['id'], valid=True)

    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))

