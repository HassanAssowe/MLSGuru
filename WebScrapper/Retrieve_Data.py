import json
from datetime import date
import requests

session_requests = requests.session()
result = []


def pullData(defaulturi, y=date.today().year,
             c=2077):  # This method pulls data on all players based on the year & specific team.
    req = defaulturi.format(str(y), str(c))
    try:
        global result
        result = json.loads(
            session_requests.get(req).content.decode()
        )
    except:
        print("Data is unavailable.")

    return result


def pullData(defaulturi, y=date.today().year):  # This method pulls data on all teams based on the specific year.
    req = defaulturi.format(y)
    try:
        global result
        result = json.loads(
            session_requests.get(req).content.decode()
        )
    except:
        print("Data is unavailable.")

    return result


def pull_data_leaders(defaulturi, stat, y=date.today().year, data_size=5):
    req = defaulturi.format(y, data_size, stat)
    try:
        global result
        result = json.loads(
            session_requests.get(req).content.decode()
        )
    except:
        print("Data is unavailable.")

    return result
