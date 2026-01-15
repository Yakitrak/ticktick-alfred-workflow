"""OpenAI client for task parsing."""

import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional
import requests

OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

# JSON Schema for structured output
TASK_RESPONSE_SCHEMA = {
    "name": "task_parse_result",
    "strict": True,
    "schema": {
        "type": "object",
        "properties": {
            "title": {
                "type": "string",
                "description": "Clear, actionable task title in imperative form"
            },
            "due_date": {
                "type": ["string", "null"],
                "description": "Due date in ISO 8601 format (yyyy-MM-ddTHH:mm:ss+0000) or null"
            },
            "repeat_flag": {
                "type": ["string", "null"],
                "description": "Repeat pattern in RRULE format or null"
            },
            "is_all_day": {
                "type": "boolean",
                "description": "True if no specific time was mentioned"
            },
            "priority": {
                "type": "integer",
                "description": "Priority: 0=normal, 1=low, 5=high"
            }
        },
        "required": ["title", "due_date", "repeat_flag", "is_all_day", "priority"],
        "additionalProperties": False
    }
}


@dataclass
class TaskParseResult:
    """Parsed task from natural language input."""
    title: str
    due_date: Optional[str] = None
    repeat_flag: Optional[str] = None
    is_all_day: bool = False
    priority: int = 0

    def to_api_dict(self) -> dict:
        """Convert to TickTick API format."""
        data = {"title": self.title}
        if self.due_date:
            data["dueDate"] = self.due_date
            data["isAllDay"] = self.is_all_day
        if self.repeat_flag:
            data["repeatFlag"] = self.repeat_flag
        if self.priority:
            data["priority"] = self.priority
        return data


def _get_example_dates(current_date: str, current_weekday: str) -> dict:
    """Calculate real dates for prompt examples."""
    base = datetime.strptime(current_date, "%Y-%m-%d")
    tomorrow = (base + timedelta(days=1)).strftime("%Y-%m-%d")

    weekdays = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
                "Friday": 4, "Saturday": 5, "Sunday": 6}
    current_wd = weekdays[current_weekday]

    # Next Wednesday (2 = Wednesday)
    days_until_wed = (2 - current_wd) % 7 or 7
    next_wed = (base + timedelta(days=days_until_wed)).strftime("%Y-%m-%d")

    # Next Monday (0 = Monday)
    days_until_mon = (0 - current_wd) % 7 or 7
    next_mon = (base + timedelta(days=days_until_mon)).strftime("%Y-%m-%d")

    return {
        "tomorrow": tomorrow,
        "next_wednesday": next_wed,
        "next_monday": next_mon
    }


def _build_system_prompt(current_date: str, current_weekday: str, timezone: str) -> str:
    """Build system prompt for task parsing."""
    dates = _get_example_dates(current_date, current_weekday)
    return f"""You are a task parser for a todo app. Extract structured task data from natural language input.

CURRENT CONTEXT:
- Today's date: {current_date}
- Today's weekday: {current_weekday}
- Timezone: {timezone}

RULES:
1. Extract a clear, actionable task title (imperative form):
   - "I need to order curtains" -> "Order curtains"
   - "want to run every wednesday" -> "Run"
   - "buy milk tomorrow" -> "Buy milk"
   - "need to call mom" -> "Call mom"

2. Parse date/time to ISO 8601 format (yyyy-MM-ddTHH:mm:ss+0000):
   - "today" = current day
   - "tomorrow" = next day
   - "day after tomorrow" = current date + 2 days
   - "at 7pm" / "by 7pm" = 19:00:00
   - "at noon" / "at lunch" = 13:00:00
   - "in the morning" = 09:00:00
   - "in the evening" = 18:00:00
   - "at night" = 23:00:00
   - "in an hour" = current time + 1 hour
   - "next week" = current date + 7 days
   - "on monday" = next Monday
   - If time not specified but date is -> is_all_day = true, time = 00:00:00
   - If neither date nor time specified -> due_date = null

3. Parse repeat patterns to RRULE format:
   - "every day" / "daily" -> RRULE:FREQ=DAILY
   - "every week" / "weekly" -> RRULE:FREQ=WEEKLY
   - "every month" / "monthly" -> RRULE:FREQ=MONTHLY
   - "every year" / "yearly" -> RRULE:FREQ=YEARLY
   - "every wednesday" -> RRULE:FREQ=WEEKLY;BYDAY=WE
   - "every monday" -> RRULE:FREQ=WEEKLY;BYDAY=MO
   - "every weekend" -> RRULE:FREQ=WEEKLY;BYDAY=SA,SU
   - "every weekday" / "on weekdays" -> RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR
   - "every monday and wednesday" -> RRULE:FREQ=WEEKLY;BYDAY=MO,WE

   Day codes: MO=Monday, TU=Tuesday, WE=Wednesday, TH=Thursday, FR=Friday, SA=Saturday, SU=Sunday

   For recurring tasks, set due_date to the FIRST occurrence.

4. Priority extraction:
   - "urgent" / "important" / "ASAP" / "very important" -> priority = 5
   - "not urgent" / "someday" / "low priority" -> priority = 1
   - Default -> priority = 0

EXAMPLES:
- "order curtains tomorrow by 7pm" -> title="Order curtains", due_date="{dates['tomorrow']}T19:00:00+0000", is_all_day=false
- "run every wednesday at noon" -> title="Run", due_date="{dates['next_wednesday']}T13:00:00+0000", repeat_flag="RRULE:FREQ=WEEKLY;BYDAY=WE"
- "urgent call mom" -> title="Call mom", due_date=null, priority=5
- "take vitamins every morning" -> title="Take vitamins", due_date="{dates['tomorrow']}T09:00:00+0000", repeat_flag="RRULE:FREQ=DAILY"
- "buy milk" -> title="Buy milk", due_date=null, is_all_day=true
- "meeting on monday at 10am" -> title="Meeting", due_date="{dates['next_monday']}T10:00:00+0000"

IMPORTANT: Calculate actual dates based on today's date and weekday from CURRENT CONTEXT."""


def parse_task_with_llm(
    user_input: str,
    api_key: str,
    current_date: str,
    current_weekday: str,
    timezone: str = "+0000",
    model: str = "gpt-4o-mini"
) -> TaskParseResult:
    """Parse natural language task input using OpenAI.

    Args:
        user_input: Natural language task description
        api_key: OpenAI API key
        current_date: Current date in ISO format (YYYY-MM-DD)
        current_weekday: Current weekday in English (Monday, Tuesday, etc.)
        timezone: Timezone offset (default: +0000)
        model: OpenAI model to use (default: gpt-4o-mini)

    Returns:
        TaskParseResult with extracted fields
    """
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": _build_system_prompt(current_date, current_weekday, timezone)
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        "temperature": 0.1,
        "max_tokens": 500,
        "response_format": {
            "type": "json_schema",
            "json_schema": TASK_RESPONSE_SCHEMA
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    try:
        response = requests.post(
            OPENAI_API_URL,
            json=payload,
            headers=headers,
            timeout=15
        )

        if response.status_code != 200:
            return _fallback_parse(user_input)

        result = response.json()
        content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
        data = json.loads(content)

        return TaskParseResult(
            title=data.get("title", user_input),
            due_date=data.get("due_date"),
            repeat_flag=data.get("repeat_flag"),
            is_all_day=data.get("is_all_day", False),
            priority=data.get("priority", 0)
        )

    except Exception:
        return _fallback_parse(user_input)


def _fallback_parse(user_input: str) -> TaskParseResult:
    """Simple fallback when LLM is unavailable."""
    return TaskParseResult(
        title=user_input,
        due_date=None,
        repeat_flag=None,
        is_all_day=True,
        priority=0
    )
