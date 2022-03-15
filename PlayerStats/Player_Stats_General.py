import Player


class Player_Stats_General(Player):
    def __init__(self, club, games_played, games_started, mins, goals, pass_percentage, assists, shots, shots_on_target, tackles_won, fouls_committed,
                 fouls_suffered, total_offsides, yellow_cards, red_cards):

        self.shots_on_target = shots_on_target
        self.red_cards = red_cards
        self.yellow_cards = yellow_cards
        self.total_offsides = total_offsides
        self.fouls_suffered = fouls_suffered
        self.fouls_committed = fouls_committed
        self.tackles_won = tackles_won
        self.shots = shots
        self.assists = assists
        self.pass_percentage = pass_percentage
        self.goals = goals
        self.mins = mins
        self.games_started = games_started
        self.games_played = games_played
        self.club = club
        

