#!/usr/bin/env python3

import sys
from ualfred import Workflow, ICON_WARNING
from api.auth import fetch_access_token

def main(wf):
    code = wf.args[0]
    token = fetch_access_token(code)
    wf.logger.debug('token: %s' % token)
    wf.store_data('token', token)
    wf.add_item('Token stored')

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))


