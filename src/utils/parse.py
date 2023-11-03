import datetime

from utils.constants import PRETTY_DATE_FORMAT, PRETTY_TIME_FORMAT

date_mappings = {
    'today': (0, "Today"),
    'tod': (0, "Today"),
    'tomorrow': (1, "Tomorrow"),
    'tom': (1, "Tomorrow"),
    'next week': (7, "Next Week"),
    'nw': (7, "Next Week"),
    'next month': (30, "Next Month"),
    'nm': (30, "Next Month"),
}


def parse_new_task(query):
    if ',' not in query:
        return query, None, None

    task_name, due_date = query.split(',')
    if not due_date:
        return task_name, None, None

    task_due_formatted, task_due_pretty = parse_due_date(due_date.strip())
    return task_name, task_due_formatted, task_due_pretty


def parse_due_date(due_datetime):
    if due_datetime in date_mappings:
        days, pretty = date_mappings[due_datetime]
        due_datetime = datetime.datetime.now() + datetime.timedelta(days=days)
        return due_datetime.isoformat(), pretty

    formats_to_try = [
        PRETTY_DATE_FORMAT,
        PRETTY_DATE_FORMAT + ' ' + PRETTY_TIME_FORMAT,
    ]

    for fmt in formats_to_try:
        try:
            due_datetime = datetime.datetime.strptime(due_datetime, fmt)
            return due_datetime.isoformat(), due_datetime.strftime(PRETTY_DATE_FORMAT + ' ' + PRETTY_TIME_FORMAT)
        except ValueError:
            pass
    return None, None
