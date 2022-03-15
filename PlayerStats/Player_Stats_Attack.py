import Player


class Player_Stats_Attack(Player):
    def __init__(self, goals, goals_inside, goals_outside, goals_per_game, headed_goals, penalty_goals, penalty_taken, pk_percentage, shots, shots_on_target, shot_percentage,
    shot_conversion, sucessful_dribbles, dribble_percentage):
        
        self.dribble_percentage = dribble_percentage
        self.sucessful_dribbles = sucessful_dribbles
        self.shot_conversion = shot_conversion
        self.shot_percentage = shot_percentage
        self.shots_on_target = shots_on_target
        self.shots = shots
        self.pk_percentage = pk_percentage
        self.penalty_taken = penalty_taken
        self.penalty_goals = penalty_goals
        self.headed_goals = headed_goals
        self.goals_per_game = goals_per_game
        self.goals_outside = goals_outside
        self.goals_inside = goals_inside
        self.goals = goals
