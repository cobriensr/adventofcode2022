"""Standard imports"""

# The Elves begin to set up camp on the beach.
# To decide whose tent gets to be closest to the snack storage,
# a giant Rock Paper Scissors tournament is already in progress.

# Rock Paper Scissors is a game between two players.
# Each game contains many rounds; in each round,
# the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape.
# Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper,
# and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

# Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide
# (your puzzle input) that they say will be sure to help you win.
# "The first column is what your opponent is going to play:
# A for Rock, B for Paper, and C for Scissors. The second column--"
# Suddenly, the Elf is called away to help with someone's tent.

# The second column, you reason, must be what you should play in response:
# X for Rock, Y for Paper, and Z for Scissors.
# Winning every time would be suspicious, so the responses must have been carefully chosen.

# The winner of the whole tournament is the player with the highest score.
# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

# Since you can't be sure if the Elf is trying to help you or trick you,
# you should calculate the score you would get if you were to follow the strategy guide.

# For example, suppose you were given the following strategy guide:

# A Y
# B X
# C Z

# This strategy guide predicts and recommends the following:

# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y).
# This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X).
# This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

# In this example, if you were to follow the strategy guide,
# you would get a total score of 15 (8 + 1 + 6).

# What would your total score be if everything goes exactly according to your strategy guide?

#create dictionaries for plays, shapes and outcomes#

opponent_plays = {
                    "A" : "Rock",
                    "B" : "Paper",
                    "C" : "Scissors"
                }

you_play = {
            "X" : "Rock",
            "Y" : "Paper",
            "Z" : "Scissors"
        }

shape_scores = {
                "Rock" : 1,
                "Paper" : 2,
                "Scissors" : 3
            }

outcome_scores = {
                    "Loss" : 0,
                    "Draw" : 3,
                    "Win" : 6
                }


def extract_strategy_guide_data(file:str) -> list:
    """extracts the strategy guide from the file"""
    strategy_guide_scores = []
    with open(file, 'r', encoding='utf-8') as data_file:
        for line in data_file:
            strategy_guide_scores.append(line.replace("\n", "").split())
        return strategy_guide_scores

extracted_data = extract_strategy_guide_data(file="./day2/day2_puzzle1_data.txt")

def map_values(values:list) -> list:
    """map shapes to letters"""
    shapes = []
    for item in values:
        shapes.append([opponent_plays[item[0]], you_play[item[1]]])
    return shapes

mapped_values = map_values(values=extracted_data)

def map_points(points: list) -> list:
    """map points to each shape"""
    shape_points = []
    for item in points:
        shape_points.append(shape_scores[item[1]])
    return shape_points
point_totals = map_points(points=mapped_values)

def find_winner(games: list) -> list:
    """find winner of each game"""
    outcomes = []
    for rounds in games:
        if rounds[0] == rounds[1]:
            outcomes.append("Draw")
        if rounds[0] == "Rock" and rounds[1] == "Paper":
            outcomes.append("Win")
        elif rounds[0] == "Rock" and rounds[1] == "Scissors":
            outcomes.append("Loss")
        if rounds[0] == "Paper" and rounds[1] == "Rock":
            outcomes.append("Loss")
        elif rounds[0] == "Paper" and rounds[1] == "Scissors":
            outcomes.append("Win")
        if rounds[0] == "Scissors" and rounds[1] == "Rock":
            outcomes.append("Win")
        elif rounds[0] == "Scissors" and rounds[1] == "Paper":
            outcomes.append("Loss")
    return outcomes
game_outcomes = find_winner(games=mapped_values)

def map_scores(game_results: list) -> list:
    """map scores to the game outcomes"""
    scores = []
    for game in game_results:
        scores.append(outcome_scores[game])
    return scores

results = map_scores(game_results=game_outcomes)

def sum_scores(shape_points: list, score_results: list) -> list:
    """sum game scores with point scores"""
    total_points = []
    if len(shape_points) == len(score_results):
        for point, score in zip(shape_points, score_results):
            total_points.append(point+score)
    point_sums = sum(total_points)
    return point_sums

totals = sum_scores(shape_points=point_totals, score_results=results)

print(totals)
