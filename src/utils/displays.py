from datetime import datetime, timedelta
from utils.constants import TICKTICK_API_DATETIME_FORMAT, PRETTY_DATE_FORMAT, PRETTY_TIME_FORMAT

def generate_task_display(item):
    title = item['title']
    subtitle = item['list_name'] + ' | ' + generate_date_times(item)
    return title, subtitle

def generate_date_times(item):
    dtime = item.get('dueDate')
    if not dtime:
        return 'No Due Date'
    dtime = datetime.strptime(dtime, TICKTICK_API_DATETIME_FORMAT)
    date = generate_pretty_date(dtime)
    time = generate_pretty_time(dtime)
    return date + (' ' + time if time else '')

def generate_pretty_date(date):
    now = datetime.now()
    if date.date() == now.date():
        return 'Today'
    elif date.date() == now.date() + timedelta(days=1):
        return 'Tomorrow'
    else:
        return date.strftime(PRETTY_DATE_FORMAT)

def generate_pretty_time(time):
    if time.time() != datetime.min.time():
        return time.strftime(PRETTY_TIME_FORMAT)
    else:
        return ''



