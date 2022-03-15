import Player


class Player_Stats_Defense(Player):
    def __init__(self,games_played,games_started,minutes,goals_against,clean_sheets,header_duel_percentage,duel,duel_percentage,interception):
        self.interception = interception
        self.duel_percentage = duel_percentage
        self.duel = duel
        self.header_duel_percentage = header_duel_percentage
        self.clean_sheets = clean_sheets
        self.goals_against = goals_against
        self.minutes = minutes
        self.games_started = games_started
        self.games_played = games_played
