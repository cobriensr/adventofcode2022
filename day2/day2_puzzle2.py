"""Standard imports"""

import day2_puzzle1

# The Elf finishes helping with the tent and sneaks back over to you.
# "Anyway, the second column says how the round needs to end:
# X means you need to lose, Y means you need to end the round in a draw,
# and Z means you need to win. Good luck!"

# The total score is still calculated in the same way,
# but now you need to figure out what shape to choose so the round ends as indicated.
# The example above now goes like this:

# In the first round, your opponent will choose Rock (A),
# and you need the round to end in a draw (Y),
# so you also choose Rock. This gives you a score of 1 + 3 = 4.
# In the second round, your opponent will choose Paper (B),
# and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
# In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

# Now that you're correctly decrypting the ultra top secret strategy guide,
# you would get a total score of 12.

# Following the Elf's instructions for the second column,
# what would your total score be if everything goes exactly according to your strategy guide?

#create dictionaries for plays, shapes and outcomes

opponent_plays = {
                    "A" : "Rock",
                    "B" : "Paper",
                    "C" : "Scissors"
                }

you_play = {
            "X" : "Loss",
            "Y" : "Draw",
            "Z" : "Win"
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

extracted_data = day2_puzzle1.extract_strategy_guide_data("./day2/day2_puzzle2_data.txt")

def find_correct_outcome(games:list) -> list:
    """determine what the appropriate play is"""
    results = []
    for game in games:
        if game[1] == "Y":
            results.append([game[0], opponent_plays[game[0]]])
        if game[1] == "X" and game[0] == "A":
            results.append([game[0], opponent_plays["C"]])
        if game[1] == "X" and game[0] == "B":
            results.append([game[0], opponent_plays["A"]])
        if game[1] == "X" and game[0] == "C":
            results.append([game[0], opponent_plays["B"]])
        if game[1] == "Z" and game[0] == "A":
            results.append([game[0], opponent_plays["B"]])
        if game[1] == "Z" and game[0] == "B":
            results.append([game[0], opponent_plays["C"]])
        if game[1] == "Z" and game[0] == "C":
            results.append([game[0], opponent_plays["A"]])
    return results

outcomes = find_correct_outcome(games=extracted_data)

def outcome_points(determinations: list) -> list:
    """score each game outcome"""
    game_points = []
    for result in determinations:
        if result[1] == "X":
            game_points.append(outcome_scores["Loss"])
        elif result[1] == "Y":
            game_points.append(outcome_scores["Draw"])
        else:
            game_points.append(outcome_scores["Win"])
    return game_points

total_outcomes = outcome_points(determinations=extracted_data)

def map_shapes(instances: list) -> list:
    """map shapes to the opponent play"""
    mappings = []
    for instance in instances:
        mappings.append([opponent_plays[instance[0]], instance[1]])
    return mappings

sets = map_shapes(instances=outcomes)

def map_points(rounds: list) -> list:
    """map shape points to my plays"""
    points = []
    for occurrance in rounds:
        points.append(shape_scores[occurrance[1]])
    return points

mapped_points = map_points(rounds=sets)

def sum_scores(shape_points: list, score_results: list) -> list:
    """sum game scores with point scores"""
    total_points = []
    if len(shape_points) == len(score_results):
        for point, score in zip(shape_points, score_results):
            total_points.append(point+score)
    point_sums = sum(total_points)
    return point_sums

totals = sum_scores(shape_points=total_outcomes, score_results=mapped_points)

print(totals)
