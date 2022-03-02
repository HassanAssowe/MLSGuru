class Club_Stats_Attack:
    def __init__(self, goals, goals_inside, goals_outside, headed_goals, pk_goals, pk_attempts, pk_perc,
                 shots, shots_on_target, shot_accuracy, assists, corners_taken, atk_assists):

        self.goals = goals
        self.goals_inside = goals_inside
        self.goals_outside = goals_outside
        self.headed_goals = headed_goals

        self.pk_goals = pk_goals
        self.pk_attempts = pk_attempts
        self.pk_perc = pk_perc

        self.shots = shots
        self.shots_on_target = shots_on_target
        self.shot_accuracy = shot_accuracy

        self.assists = assists

        self.corners_taken = corners_taken
        self.atk_assists = atk_assists


