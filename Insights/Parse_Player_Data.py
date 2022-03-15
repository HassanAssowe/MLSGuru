from datetime import datetime, date

from PlayerStats import Player
from PlayerStats import Player_Stats_General

def parse_player_info(data):
    position = "{} {} {} {}".format(
        data['position_generic'],
        '' if data['position_side'] == 'Unknown' and data['position_specific'] == 'Unknown' else '-',
        '' if data['position_side'] == 'Unknown' else data['position_side'],
        '' if data['position_specific'] == 'Unknown' else data['position_specific']
    )

    found_player = (
        Player.player(
            data.get("player").get("first_name"),
            data.get("player").get("last_name"),
            datetime.datetime.fromtimestamp(
                data.get("player").get("birth_date") / 1e3
            ),
            date.today().year
            - datetime.datetime.fromtimestamp(
                data.get("player").get("birth_date") / 1e3).year,
            data.get("player").get("height"),
            data.get("player").get("birth_country"),
            position,
            data.get("player").get("preferred_foot"),
            data.get("club_stats_general").get("name")
        )
    )
    return found_player

def parse_player_general(data):
    found_player = Player_Stats_General.Player_Stats_General(
            data.get("club").get("name"),
            data.get("regular_season_statistics").get("games_played"),
            data.get("regular_season_statistics").get("games_started"),
            data.get("regular_season_statistics").get("mins_played"),
            data.get("regular_season_statistics").get("goals"),
            data.get("regular_season_statistics").get("accurate_pass_per"),
            data.get("regular_season_statistics").get("goal_assist"),
            data.get("regular_season_statistics").get("accurate_pass_per"),
            0,
            data.get("regular_season_statistics").get("accurate_shooting_per"),
            0,
            data.get("regular_season_statistics").get("fk_foul_won"),
            data.get("regular_season_statistics").get("fk_foul_lost"),
            0,
            data.get("regular_season_statistics").get("yellow_card"),
            data.get("regular_season_statistics").get("red_card"))

    return found_player

