import os

TICKTICK_API_URL = 'https://api.ticktick.com/open/v1'
TICKTICK_TOKEN='Bearer ' + os.getenv('TICKTICK_TOKEN')
HEADERS = {"Authorization": TICKTICK_TOKEN}
