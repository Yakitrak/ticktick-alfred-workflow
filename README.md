# TickTick Alfred Workflow

This workflow allows you to search, open, add, and complete tasks in [TickTick](https://ticktick.com/)

<img src="/docs/main.gif" width="500" height="400" alt="TickTick Alfred Workflow" />

[View in Alfred Forums](https://www.alfredforum.com/topic/21114-ticktick-workflow-interact-with-your-tasks-and-lists/)

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
  - [OpenAI Smart Parsing (Optional)](#openai-smart-parsing-optional)
- [Usage](#usage)
  - [Lists](#lists)
    - [List Search](#list-search-tls-query)
    - [Create List](#create-list-tln-list-name)
  - [Tasks](#tasks)
    - [Task Search](#task-search-tts-query)
    - [Complete Task](#complete-task)
    - [Create Task](#create-task-ttn-task-name-due-date)
  - [Sync](#sync-tsync)
  - [Calendar](#calendar)
    - [Calendar (Day)](#calendar-day-tcd)
    - [Calendar (Week)](#calendar-week-tcw)
    - [Calendar (Month)](#calendar-month-tcm)
- [Current Limitations](#current-limitations)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Installation

Click [here](https://github.com/yakitrak/ticktick-alfred-workflow/releases/latest) to download the latest version of the workflow.
Or you can build it yourself by cloning this repo into your Alfred workflows directory. To run this workflow,
you will need to have the [Alfred Powerpack](https://www.alfredapp.com/powerpack/) and python3 installed.

Libraries such as python3 and parsedatetime are included in the workflow, so you don't need to install them yourself.

Please note, this workflow is not an official TickTick product and is not affiliated with TickTick in any way.

## Setup

1. Go to [https://developer.ticktick.com/manage](https://developer.ticktick.com/manage) and
   create a new app with any name you want. You'll be asked for a redirect url, please enter in `http://localhost`.
2. Now you should have a "Client ID" and "Client Secret". Copy these values.
3. Here it also asks for "OAuth redirect URL", please enter `http://localhost` and save.
4. Go to "Configure Workflow" button on this workflow on Alfred, paste the "Client ID" and "Client Secret"
5. Using Alfred, type in `tsetup1` and authorise the workflow, you'll be redirected to
   `http://localhost?code=xxxxx`. Please copy the code from the url.
6. Using Alred, type in `tsetup2` followed by the code from the step 1 (e.g. `tsetup2 xxxxx`). You are now ready to use the workflow!

### OpenAI Smart Parsing (Optional)

Enable AI-powered natural language parsing for task creation:

1. Get an API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Go to "Configure Workflow" in Alfred and paste your API key in the "OpenAI API Key" field

With OpenAI enabled, you can create tasks using natural language:
- `ttn buy milk tomorrow at 5pm` → Creates "Buy milk" with due date
- `ttn run every wednesday at noon` → Creates "Run" with weekly recurrence
- `ttn call mom urgent` → Creates "Call mom" with high priority

The AI extracts:
- **Task title** from conversational input
- **Due date/time** from natural language ("tomorrow", "next monday", "in 2 hours")
- **Repeat patterns** converted to RRULE format ("every day", "weekly on fridays")
- **Priority** from keywords ("urgent", "important", "ASAP")

## Usage

### Lists

#### List Search `tls <query>`

Search for a list in TickTick. Pressing enter will open the list in TickTick.

<img src="/docs/list_search.png"  width="500" alt="List Search" />

#### Create List `tln <list-name>`

Create a new list in TickTick with the given name.

<img src="/docs/create_list.png"  width="500" alt="Create List" />

### Tasks

#### Task Search `tts <query>`

Search for a task in TickTick. Pressing enter will open the task in TickTick.

<img src="/docs/task_search.png"  width="500" alt="Task Search" />

You can search for tasks in a few different ways:

- `tts` - Search for all tasks
- `tts <task-name>` - Search for tasks with the given name
- `tts <list-name>` - Search for tasks in the given list
- `tts @today` or `tts @tod` - Search for tasks due today
- `tts @tomorrow` or `tts @tom` - Search for tasks due tomorrow
- `tts @thisweek` or `tts @tw` - Search for tasks due this week

As mentioned in the [Current Limitations](#current-limitations) section, you cannot search for tasks in Inbox at the moment.

#### Complete Task

You can complete a task by pressing `cmd + enter` when selecting a task in the search results from the [Task Search](#task-search-tts-query) command.

#### Create Task `ttn <task-name>, <due-date>`

Create a new task in TickTick with the given name.

<img src="/docs/create_task.png" width="500"   alt="Create Task" />

**Basic mode** (without OpenAI): Add an optional comma and include a due date:

- `ttn Do laundry`
- `ttn Do the laundry, tomorrow at 5pm`
- `ttn Do the laundry, next week`
- `ttn Do the laundry, monday`

**Smart mode** (with OpenAI): Just type naturally without commas:

- `ttn buy groceries tomorrow evening` → "Buy groceries" due tomorrow at 6pm
- `ttn meeting with John next monday at 10am` → "Meeting with John" due Monday 10:00
- `ttn take vitamins every morning` → "Take vitamins" repeating daily at 9am
- `ttn urgent fix the bug` → "Fix the bug" with high priority

See [OpenAI Smart Parsing](#openai-smart-parsing-optional) for setup instructions.

As mentioned in the [Current Limitations](#current-limitations) section, you can only add tasks to the Inbox list at the moment.

### Sync `tsync`

<img src="/docs/sync.png" width="500" alt="sync" />

Sync your TickTick account with the workflow by clearing the cache and fetching your latest lists and tasks. This is done automatically when:

- You search for a list or task, and it's been more than 5 minutes since the last sync
- You create a new list or task
- You complete a task

Once you run this command, please wait a moment for the sync to complete before searching for a list or task. This can take a few seconds if you have a lot of lists.

### Calendar

<img src="/docs/calendar.png" width="500" alt="Calendar" />

#### Calendar (Day) `tcd`

Open the calendar in TickTick, in the day view.

#### Calendar (Week) `tcw`

Open the calendar in TickTick, in the week view.

#### Calendar (Month) `tcm`

Open the calendar in TickTick, in the month view.

## Current Limitations

- Task search can take a while to load if you have a lot of lists - this is a limitation of the TickTick API as it requires a separate request for each list. Although once loaded it should be cached.
- You cannot search for tasks in Inbox - this is a limitation of the TickTick API.
- You cannot add tasks to any list other than Inbox - this is a limitation of the TickTick API.

As the TickTick API is quite new, I'm hoping these limitations will be fixed in the future.

## Contributing

If you have any issues or feature requests, please open an [issue](https://github.com/yakitrak/ticktick-alfred-workflow/issues/new/choose) or a [pull request](https://github.com/Yakitrak/ticktick-alfred-workflow/pulls).

## Acknowledgements

- [TickTick API](https://developer.ticktick.com/api#/openapi) - The TickTick API used to build this workflow.
- [ualfred](https://github.com/ischaojie/ualfred) & [Alfred Workflow](https://github.com/deanishe/alfred-workflow) - The python3 library fork and the Alfred workflow library used to build this workflow.
- [parsedatetime](https://github.com/bear/parsedatetime/) - Used to parse natural language dates and times for creating tasks.
- [OpenAI API](https://platform.openai.com/) - Powers the smart natural language task parsing feature.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
