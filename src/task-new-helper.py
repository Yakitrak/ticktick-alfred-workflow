import sys
import os
import json
from datetime import datetime
from ualfred import Workflow
from utils.parse import parse_new_task


def main(wf):
    query = " ".join(wf.args)

    api_key = os.getenv("openai_api_key")

    if api_key:
        from llm.openai import parse_task_with_llm

        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_weekday = now.strftime("%A")  # Monday, Tuesday, etc.

        result = parse_task_with_llm(
            user_input=query,
            api_key=api_key,
            current_date=current_date,
            current_weekday=current_weekday
        )

        subtitle_parts = []

        if result.due_date:
            due_display = _format_due_date(result.due_date)
            subtitle_parts.append(f"Due: {due_display}")

        if result.repeat_flag:
            repeat_display = _format_repeat(result.repeat_flag)
            subtitle_parts.append(f"Repeat: {repeat_display}")

        if result.priority > 0:
            priority_display = {1: "Low", 3: "Medium", 5: "High"}.get(result.priority, "")
            if priority_display:
                subtitle_parts.append(f"Priority: {priority_display}")

        subtitle = " | ".join(subtitle_parts) if subtitle_parts else "No date"
        arg = json.dumps(result.to_api_dict())

        wf.add_item(
            title=f"Create: {result.title}",
            subtitle=subtitle,
            arg=arg,
            valid=True
        )
    else:
        if query.count(',') > 1:
            wf.add_item(
                title="Too many commas",
                subtitle="Please only use one comma to separate task name and due date",
                valid=True
            )
            wf.send_feedback()
            return

        task_name, task_due_formatted, task_due_pretty = parse_new_task(query)

        title = "TickTick Task New: {}".format(task_name)
        subtitle = "Create a new task with name '{}'".format(task_name)
        arg = "{}|{}".format(task_name, task_due_formatted) if task_due_formatted else task_name

        if task_due_pretty:
            subtitle += " and due {}".format(task_due_pretty)

        wf.add_item(title=title, subtitle=subtitle, arg=arg, valid=True)

    wf.send_feedback()


def _format_due_date(iso_date: str) -> str:
    """Format ISO date for display."""
    try:
        clean_date = iso_date.replace('+0000', '+00:00')
        dt = datetime.fromisoformat(clean_date)
        if dt.hour == 0 and dt.minute == 0:
            return dt.strftime("%d/%m/%y")
        return dt.strftime("%d/%m/%y %H:%M")
    except Exception:
        return iso_date


def _format_repeat(rrule: str) -> str:
    """Format RRULE for display."""
    if not rrule:
        return ""

    rule = rrule.replace("RRULE:", "")
    parts = dict(p.split("=") for p in rule.split(";") if "=" in p)

    freq = parts.get("FREQ", "")
    byday = parts.get("BYDAY", "")

    freq_map = {
        "DAILY": "Daily",
        "WEEKLY": "Weekly",
        "MONTHLY": "Monthly",
        "YEARLY": "Yearly"
    }

    day_map = {
        "MO": "Mon", "TU": "Tue", "WE": "Wed",
        "TH": "Thu", "FR": "Fri", "SA": "Sat", "SU": "Sun"
    }

    result = freq_map.get(freq, freq)
    if byday:
        days = [day_map.get(d, d) for d in byday.split(",")]
        result += f" ({', '.join(days)})"

    return result


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
