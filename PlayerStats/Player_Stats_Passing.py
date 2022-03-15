import Player


class Player_Stats_Passing(Player):
    def __init__(self, completed_passes, total_passes, pass_percentage, fwd_zone_pass, bak_zone_pass, crosses, assists, assists_per_game, atk_assists, long_balls, short_passes, turnovers):
        self.assists = assists
        self.turnovers = turnovers
        self.short_passes = short_passes
        self.long_balls = long_balls
        self.atk_assists = atk_assists
        self.assists_per_game = assists_per_game
        self.crosses = crosses
        self.bak_zone_pass = bak_zone_pass
        self.fwd_zone_pass = fwd_zone_pass
        self.pass_percentage = pass_percentage
        self.total_passes = total_passes
        self.completed_passes = completed_passes
