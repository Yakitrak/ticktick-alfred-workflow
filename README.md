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
`tls <query>` - Search for a list in TickTick. Pressing enter will open the list in TickTick.

`tln <query>` - Create a new list in TickTick. Pressing enter will open the list in TickTick.

### Tasks
`tts <query>` - Search for a task in TickTick. 
- You can search by task name, list name, or "@today / @tod" or "@tomorrow / @tom" to search for tasks due today or tomorrow respectively.
- Pressing enter will open the task in TickTick. You can also press `cmd + enter` to complete the task.
- You can use `@today` or `@tomorrow` to search for tasks due today or tomorrow respectively.

`ttn <query>` - Add a new task to TickTick`. Pressing enter will only add the test, but pressing `cmd + enter` will
open the task in TickTick.

### Calendar
`tcd` - Open the calendar in TickTick, in the day view.
`tcw` - Open the calendar in TickTick, in the week view.
`tcm` - Open the calendar in TickTick, in the month view.

## Contributing
If you have any issues or feature requests, please open an [issue](https://github.com/yakitrak/ticktick-alfred-workflow/issues/new).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details








