import sys
from ualfred import Workflow
from api.list import create_list

def main(wf):
    list_name = " ".join(wf.args)
    token = wf.stored_data('access_token')
    r = create_list(token, list_name)
    if r.status_code != 200:
        print("List could not be created. Please try again.")
    else:
        wf.cache_data('lists', None)
        print('{} list created.'.format(list_name))


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))

