#!/usr/bin/env python3

import sys
from ualfred import Workflow, ICON_WARNING
from api.list import get_lists
from utils.filters import key_for_list

def main(wf):
    query = wf.args[0] if len(wf.args) else None
    lists = wf.cached_data('lists', get_lists, max_age=60)

    items = wf.filter(query, lists, key_for_list) if query else lists

    if not items:
        wf.add_item('No lists match your query', icon=ICON_WARNING)

    for item in items:
        wf.add_item(item['name'], subtitle=item['id'], arg=item['id'])

    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))

