from datetime import datetime, timedelta
from utils.constants import TICKTICK_API_DATETIME_FORMAT

def key_for_list(ttList):
    return ttList['name']

def key_for_task(ttTask):
    return '{} {}'.format(ttTask['title'], ttTask['list_name'])

def is_today(ttTask):
    if ttTask.get('dueDate', None) is None:
        return False
    dtime = datetime.strptime(ttTask['dueDate'], TICKTICK_API_DATETIME_FORMAT)
    return dtime.date() == datetime.now().date()

def is_tomorrow(ttTask):
    if ttTask.get('dueDate', None) is None:
        return False
    dtime = datetime.strptime(ttTask['dueDate'], TICKTICK_API_DATETIME_FORMAT)
    return dtime.date() == datetime.now().date() + timedelta(days=1)

def is_this_week(ttTask):
    if ttTask.get('dueDate', None) is None:
        return False
    dtime = datetime.strptime(ttTask['dueDate'], TICKTICK_API_DATETIME_FORMAT)
    return dtime.date() >= datetime.now().date() and dtime.date() <= datetime.now().date() + timedelta(days=7)

def sort_by_due_date(ttTask):
    due_date = ttTask.get('dueDate', None)
    if due_date is None:
        return 9999999999
    dtime = datetime.strptime(ttTask['dueDate'], TICKTICK_API_DATETIME_FORMAT)
    return dtime.timestamp()


