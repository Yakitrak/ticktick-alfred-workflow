import sys
from ualfred import Workflow

def main(wf):
    wf.clear_cache()
    print("Cache cleared.")


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))

