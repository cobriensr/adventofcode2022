"""Standard imports"""

import day1_puzzle1

# By the time you calculate the answer to the Elves' question
# they've already realized that the Elf carrying the most
# Calories of food might eventually run out of snacks.

# To avoid this unacceptable situation,
# the Elves would instead like to know the total Calories
# carried by the top three Elves carrying the most Calories.
# That way, even if one of those Elves runs out of snacks, they still have two backups.

# In the example above, the top three Elves are the fourth Elf (with 24000 Calories),
# then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories).
# The sum of the Calories carried by these three elves is 45000.

# Find the top three Elves carrying the most Calories.
# How many Calories are those Elves carrying in total?

def find_max_3_calories(calories:list) -> int:
    """finds the total calories of the top 3 elves"""
    sorted_calories = sorted(calories, reverse=True)
    max_3_elves_calories = sum(sorted_calories[0:3])
    return max_3_elves_calories

total = find_max_3_calories(calories=day1_puzzle1.elves_calorie_sums)

print(total)
