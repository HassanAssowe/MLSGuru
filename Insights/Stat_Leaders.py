#The Stats Leaders class allows us to pull the league leaders for a variety of stats.
#We can filter by the Top # of players for a given stat, by year so far. A list of all possible stats are found: https://pastebin.com/mbArEJKC
from datetime import date

import Insights.Parse_Player_Data
from WebScrapper import Retrieve_Data

defaultUri = 'https://stats-api.mlssoccer.com/v1/players/seasons?&season_opta_id={}&competition_opta_id=98&page_size={}&order_by=-{}&include=regular_season_statistics&include=club&include=player&order_by=player_last_name'
playerInfo = []
playerGeneral = []


def stat_leader(defaultUri, stat, y=date.today().year, data_size=5):
    result = Retrieve_Data.pull_data_leaders(defaultUri,stat,y,data_size)

    if result != None:
        for i in result:
            playerInfo.append(Insights.Parse_Player_Data.parse_player_info(i))
            playerGeneral.append(Insights.Parse_Player_Data.parse_player_general(i))

        return playerGeneral

