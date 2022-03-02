#This file is responsible for Standings retrieval & management.
import json
from datetime import date

import requests

result = []
easternConference = []
westernConference = []
session_requests = requests.session()
defaultUri = 'https://sportapi.mlssoccer.com/api/standings/live?isLive=true&seasonId={}&competitionId=98'


def pullData(y=date.today().year):  # This method pulls data on all teams based on the specific year.
    req = defaultUri.format(y)
    try:
        global result
        result = json.loads(
            session_requests.get(req).content.decode()
        )
    except:
        print("Information is currently unavailable.")


def parseData(y=date.today().year): #Parsing data by Eastern & Western Conferences.
    pullData(y)

    for i in result:
        if i.get('group_id') == 'East':
            easternConference.append(i)
        else:
            westernConference.append(i)

parseData()
print(easternConference)