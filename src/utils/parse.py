import datetime
def parse_new_task(query):
    due_date = ''
    if 'due:' in query:
        task_name, due_date = query.split('due:')
        due_date = parse_due_date(due_date)
    else:
        task_name = query
    return {
        'name': task_name,
        'due_date': due_date
    }

def parse_due_date(due_date):
    if due_date == 'today' or due_date == 'tod':
        return datetime.datetime.now().strftime('%Y-%m-%d')
    elif due_date == 'tomorrow' or due_date == 'tom':
        return (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    elif due_date == 'next week' or due_date == 'next wk':
        return (datetime.datetime.now() + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    elif due_date == 'next month' or due_date == 'next mon':
        return (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')
    elif len(due_date) == 16:
        try:
            datetime.datetime.strptime(due_date, '%d-%m-%y %H:%M')
            return due_date
        except ValueError:
            pass
    return due_date
