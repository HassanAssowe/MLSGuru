class Club_Stats_Defense:
    def __init__(self, id, goals_against, shots_against, clean_sheets, save_perc, head_duel_perc, duel_perc, interceptions,
                 pk_conceded, pk_saves, pk_save_perc):
        self.id = id

        self.goals_against = goals_against
        self.shots_against = shots_against
        self.clean_sheets = clean_sheets
        self.save_perc = save_perc
        self.head_duel_perc = head_duel_perc
        self.duel_perc = duel_perc
        self.interceptions = interceptions

        self.pk_conceded = pk_conceded
        self.pk_saves = pk_saves
        self.pk_save_perc = pk_save_perc