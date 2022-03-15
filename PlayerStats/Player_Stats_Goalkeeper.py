import Player


class Player_Stats_Goalkeeper(Player):
    def __init__(self,games_played,games_started,minutes,goals_against,goals_conceded_avg,saves,save_percentage,pk_faced,pk_conceded,pass_percentage,long_ball_percentage,clearances,
                 clean_sheets, wins, losses, ties, win_percentage):
        self.win_percentage = win_percentage
        self.ties = ties
        self.losses = losses
        self.wins = wins
        self.clean_sheets = clean_sheets
        self.clearances = clearances
        self.long_ball_percentage = long_ball_percentage
        self.pass_percentage = pass_percentage
        self.pk_conceded = pk_conceded
        self.pk_faced = pk_faced
        self.save_percentage = save_percentage
        self.saves = saves
        self.goals_conceded_avg = goals_conceded_avg
        self.goals_against = goals_against
        self.minutes = minutes
        self.games_started = games_started
        self.games_played = games_played
        