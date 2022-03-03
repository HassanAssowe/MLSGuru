from ClubStats.Club import Club


class Club_Stats_General:

    # init method or constructor
    def __init__(self, opta_id, position, name, games_played, points, wins, losses, ties, goals, goals_against, goals_difference):
        self.opta_id = opta_id
        self.position = position
        
        self.name = name
        self.games_played = games_played
        self.points = points
        self.wins = wins
        self.losses = losses
        self.ties = ties

        self.goals = goals
        self.goals_against = goals_against
        self.goals_difference = goals_difference



    def get_opta_id(self):
        return self.opta_id


    def opta_id(self, value):
        self.opta_id = value

    def get_name(self):
        return self.name

    def name(self, value):
        self.name = value

    def get_position(self):
        return self.position

    def position(self, value):
        self.position = value

    def get_games_played(self):
        return self.games_played

    def games_played(self, value):
        self.games_played = value

    def get_points(self):
        return self.points

    def points(self, value):
        self.points = value


    def get_wins(self):
        return self.wins

    def wins(self, value):
        self.wins = value

    def get_losses(self):
        return self.losses

    def losses(self, value):
        self.losses = value

    def get_ties(self):
        return self.ties

    def ties(self, value):
        self.ties = value


    def get_goals(self):
        return self.goals

    def goals(self, value):
        self.goals = value


    def get_goals_against(self):
        return self.goals_against

    def goals_against(self, value):
        self.goals_against = value


    def get_goals_difference(self):
        return self.goals_difference

    def goals_difference(self, value):
        self.goals_difference = value