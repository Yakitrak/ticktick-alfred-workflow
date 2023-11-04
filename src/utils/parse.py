import parsedatetime
from utils.constants import PRETTY_DATE_FORMAT, PRETTY_TIME_FORMAT
import datetime

def parse_new_task(query):
    if ',' not in query:
        return query, None, None

    task_name, due_date = query.split(',')
    if not due_date:
        return task_name, None, None

    task_due_formatted, task_due_pretty = parse_due_date(due_date.strip())
    return task_name, task_due_formatted, task_due_pretty


def parse_due_date(date_string):
    # today and tomorrow automatically changes to 9am for some reason so we mitigate it to 00:00:00
    if date_string == "today" or date_string == "tomorrow":
        date_string = date_string.replace("today", "today 00:00:00")
        date_string = date_string.replace("tomorrow", "tomorrow 00:00:00")

    try:
        cal = parsedatetime.Calendar()
        # st source time to 00:00:00 so that if time is not specified, it will be 00:00:00
        parsed_date, parse_status = cal.parseDT(date_string, sourceTime=datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
        if parse_status != 0:
            formatted_time = parsed_date.isoformat() + "+0000"
            # if time is 00:00:00, then don't show it
            pretty_time = parsed_date.strftime(PRETTY_DATE_FORMAT) + " " + parsed_date.strftime(
                PRETTY_TIME_FORMAT) if parsed_date.strftime(PRETTY_TIME_FORMAT) != "12:00AM" else parsed_date.strftime(
                PRETTY_DATE_FORMAT)

            return formatted_time, pretty_time
        else:
            return None, None
    except:
        return None, None
