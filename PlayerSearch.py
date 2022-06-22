
from WebScrapper import Retrieve_Data, Player_Data


def PlayerSearch(name):

    for x in Player_Data.teams:
        if(Player_Data.getPlayer_Info(name[0], name[1], Player_Data.teams[x]) != False):
            #We have found the player, populate Javascript information with Player data HERE WIP

