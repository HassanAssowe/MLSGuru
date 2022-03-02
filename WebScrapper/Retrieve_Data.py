import json
from datetime import date
import requests


session_requests = requests.session()
result = []

def pullData(defaultUri, y=date.today().year, c=2077):  # This method pulls data on all players based on the year & specific team.
    req = defaultUri.format(str(y), str(c))
    try:
        global result
        result = json.loads(
            session_requests.get(req).content.decode()
        )
    except:
        print("Data is unavailable.")

    return result


def pullData(defaultUri, y=date.today().year):  # This method pulls data on all teams based on the specific year.
    req = defaultUri.format(y)
    try:
        global result
        result = json.loads(
            session_requests.get(req).content.decode()
        )
    except:
        print("Data is unavailable.")

    return result