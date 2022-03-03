#This file is responsible for Standings retrieval & management.
import json
from datetime import date
import Retrieve_Data
from ClubStats.Club_Stats_General import Club_Stats_General

result = []
easternConference = []
westernConference = []
defaultUri = 'https://sportapi.mlssoccer.com/api/standings/live?isLive=true&seasonId={}&competitionId=98' #API that handles calls



def parseData(x = defaultUri, y=date.today().year): #Parsing data by Eastern & Western Conferences.
    result = Retrieve_Data.pullData(x, y)
    for i in result:
        if i.get('group_id') == 'East': #If the club is considered Eatern Conference, add it. Otherwise add it to the western conference.
            club = Club_Stats_General( #Define a GeneralStats Class and populate it with general information about a club.
                i.get('club').get("optaId"),
                i['position'],
                i.get('club').get("fullName"),
                i.get('statistics').get('total_matches'),
                i.get('statistics').get('total_points'),
                i.get('statistics').get('total_wins'),
                i.get('statistics').get('total_losses'),
                i.get('statistics').get('total_draws'),
                i.get('statistics').get('total_goals'),
                i.get('statistics').get('total_goals_conceded'),
                i.get('statistics').get('total_goal_difference')
            )
            easternConference.append(club) #Add it to conference.

        else:
            club = Club_Stats_General(  #Define a GeneralStats Class and populate it with general information about a club.
                i.get('club').get("optaId"),
                i['position'],
                i.get('club').get("fullName"),
                i.get('statistics').get('total_matches'),
                i.get('statistics').get('total_points'),
                i.get('statistics').get('total_wins'),
                i.get('statistics').get('total_losses'),
                i.get('statistics').get('total_draws'),

                i.get('statistics').get('total_goals'),
                i.get('statistics').get('total_goals_conceded'),
                i.get('statistics').get('total_goal_difference')
            )
            westernConference.append(club) #Add it to conference.


    return easternConference, westernConference #Returns General Information on clubs, by their conference & in order.

