import sys
from ualfred import Workflow

def main(wf):
    list_name = " ".join(wf.args)
    title = "TickTick List New: {}".format(list_name)
    subtitle = "Create a new list with name '{}'".format(list_name)
    wf.add_item(title=title, subtitle=subtitle, arg=list_name, valid=True)
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))

