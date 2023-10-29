from datetime import datetime, timedelta
def key_for_list(ttList):
    return ttList['name']

def key_for_task(ttTask):
    return '{} {}'.format(ttTask['title'], ttTask['list_name'])

def is_today(ttTask):
    dtime = datetime.strptime(ttTask['dueDate'], '%Y-%m-%dT%H:%M:%S.%f%z')
    return dtime.date() == datetime.now().date()

def is_tomorrow(ttTask):
    dtime = datetime.strptime(ttTask['dueDate'], '%Y-%m-%dT%H:%M:%S.%f%z')
    return dtime.date() == datetime.now().date() + timedelta(days=1)
