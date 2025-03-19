from utils import all_games_from_file, extract_year
import csv

def overtime_score(score):
    if int(score) > 200:
        return int(str(score)[:-1])
    else:
        return score

def get_game_strings(inpath):
    games = all_games_from_file(inpath)
    gamestrings = []
    for game in games:
        winner = max(game, key=lambda d: d["score"])
        loser = min(game, key=lambda d: d["score"])
        gamestring = [extract_year(str(inpath)), winner["round_of"],
                      winner["team"], winner["seed"], overtime_score(winner["score"]), 
                      loser["team"], loser["seed"], overtime_score(loser["score"])]
        gamestrings.append(gamestring)
    return gamestrings

def extract_csv_from_json(inpath, outpath):
    gamestrings = get_game_strings(inpath)
    with open(outpath, mode="w") as csv_file:
        fieldnames = ["year", "round_of", 
                      "winning_team_name", "winning_team_seed", "winning_team_score", 
                      "losing_team_name", "losing_team_seed", "losing_team_score"]
        writer= csv.writer(csv_file)
        writer.writerow(fieldnames)
        writer.writerows(row for row in gamestrings)
