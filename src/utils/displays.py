from datetime import datetime, timedelta
def generate_task_display(item):
    title = item['title']
    subtitle = item['list_name'] + ' | ' + generate_date_times(item)
    return title, subtitle

def generate_date_times(item):
    dtime = item.get('dueDate')
    if not dtime:
        return 'No Due Date'
    dtime = datetime.strptime(dtime, '%Y-%m-%dT%H:%M:%S.%f%z')
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
        return date.strftime('%d/%m/%Y')

def generate_pretty_time(time):
    if time.time() != datetime.min.time():
        return time.strftime('%I:%M%p')
    else:
        return ''



