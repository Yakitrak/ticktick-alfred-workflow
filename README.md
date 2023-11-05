# TickTick Alfred Workflow

<Screenshot-Here> 

This workflow allows you to see, open, add, and complete tasks in TickTick. 

## Installation
Click [here](https://github.com/yakitrak/ticktick-alfred-workflow/releases/latest) to download the latest version of the workflow. 
Or you can build it yourself by cloning this repo into your Alfred workflows directory. To run this workflow,
you will need to have the [Alfred Powerpack](https://www.alfredapp.com/powerpack/) installed and python3 installed.

## Setup
1. Go to [https://developer.ticktick.com/manage](https://developer.ticktick.com/manage) and 
create a new app with any name you want. You'll be asked for a redirect url, pleae enter in `http://localhost`.
2. Go to "Configure Workflow" button on this workflow on Alfred, and copy and paste the "Client ID" and "Client Secret"
3. Using Alfred, type in `tsetup1` and authorise the workflow, you'll be redirected to 
`http://localhost?code=xxxxx`.
4. Using Alred, type in `tsetup2` followed by the code from the step 1. You are now ready to use the workflow!

## Usage
### Lists
#### List Search `tls <query>`
Search for a list in TickTick. Pressing enter will open the list in TickTick.

#### Create List `tln <list-name>`
Create a new list in TickTick with the given name. 

### Tasks
#### Task Search `tts <query>`
Search for a task in TickTick. 
- You can search by task name, list name, or shortcuts:
  - `@today / @tod` - Search for tasks due today
  - `@tomorrow / @tom` - Search for tasks due tomorrow
  - `@thisweek / @wk` - Search for tasks due this week
- Pressing enter will open the task in TickTick. 
- You can also press `cmd + enter` to complete the task.

#### Create Task `ttn <task-name>, <due-date>`
Create a new task in TickTick with the given name.
- You can add an optional comma at the end and include a due date using natural language.
   - e.g. `ttn Do the laundry, tomorrow at 5pm`
   - e.g. `ttn Do the laundry, next week`

### Calendar
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
If you have any issues or feature requests, please open an [issue](https://github.com/yakitrak/ticktick-alfred-workflow/issues/new).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgements
- [ualfred](https://github.com/ischaojie/ualfred) - Used to build the alfred workflow in python3. Also thanks to the [original Alfred Workflow]()
- [parsedatetime](https://github.com/bear/parsedatetime/) - Used to parse natural language dates and times.

