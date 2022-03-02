import datetime
from PlayerStats import Player
import requests
import json
from datetime import date


teams = {
    "atlanta": 11091,
    "austin": 15296,
    "charlotte": 16629,
    "chicago": 1207,
    "cincinnati": 11504,
    "colderado": 436,
    "columbus": 454,
    "dallas": 1903,
    "d.c.": 1326,
    "houston": 1897,
    "lafc": 11690,
    "la": 1230,
    "miami": 14880,
    "minnesota": 6977,
    "montreal": 1616,
    "nashville": 15154,
    "newengland": 928,
    "newyorkcity": 9668,
    "newyork": 399,
    "philadelphia": 5513,
    "orlando": 6900,
    "portland": 1581,
    "saltlake": 1899,
    "sanjose": 1131,
    "seattle": 3500,
    "kansascity": 421,
    "toronto": 2077,
}

result = []
session_requests = requests.session()
defaultUri = 'https://stats-api.mlssoccer.com/v1/players/seasons?&season_opta_id={}&competition_opta_id=98&club_opta_id={}&order_by=-regular_season_player_season_stat_goals&include=regular_season_statistics&include=club_stats_general&include=player&order_by=player_last_name'


def pullData(y=date.today().year, c=teams.get("atlanta")):  # This method pulls data on all players based on the year & specific team.
    req = defaultUri.format(y, c)
    try:
        global result
        result = json.loads(
            session_requests.get(req).content.decode()
        )
    except:
        print("An error has occured")


def getPlayer(first_name="", last_name=""):
    if first_name == "" or last_name == "":
        print("Please input a name")

    for i in result:
        if (
                i.get("player").get("first_name").lower() == first_name.lower()
                and i.get("player").get("last_name").lower() == last_name.lower()
        ):
            position = "{} {} {} {}".format(
                i['position_generic'],
                '' if i['position_side'] == 'Unknown' and i['position_specific'] == 'Unknown' else '-',
                '' if i['position_side'] == 'Unknown' else i['position_side'],
                '' if i['position_specific'] == 'Unknown' else i['position_specific']
            )

            found_player = (
                Player.player(
                    i.get("player").get("first_name"),
                    i.get("player").get("last_name"),
                    datetime.datetime.fromtimestamp(
                        i.get("player").get("birth_date") / 1e3
                    ),
                    date.today().year
                    - datetime.datetime.fromtimestamp(
                        i.get("player").get("birth_date") / 1e3).year,
                    i.get("player").get("height"),
                    i.get("player").get("birth_country"),
                    position,
                    i.get("player").get("preferred_foot"),
                    i.get("club_stats_general").get("name")
                )
            )
            return found_player


def getAllPlayers():
    players = []

    for i in result:
        players.append(getPlayer(i.get("player").get("first_name"), i.get("player").get("last_name")))

    return players


def getPlayersByPosition(position='Forward'):
    allPlayers = getAllPlayers()

    for i in allPlayers[:]:
        if position not in i.position:
            allPlayers.remove(i)

    return allPlayers


