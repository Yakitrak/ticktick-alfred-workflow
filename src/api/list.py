from utils.constants import TICKTICK_API_URL
import requests
def get_lists(token):
    headers = {
        "Authorization": "Bearer " + token,
    }
    url = TICKTICK_API_URL + '/project'
    return requests.get(url, headers=headers).json()


def create_list(token, list_name):
    headers = {
        "Authorization": "Bearer " + token,
    }
    data = {
        "name": list_name,
    }
    url = TICKTICK_API_URL + '/project'
    return requests.post(url, headers=headers, json=data)

