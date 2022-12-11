"""Standard imports"""

# The jungle must be too overgrown and difficult to navigate in vehicles or access from the air.
# The Elves' expedition traditionally goes on foot.
# As your boats approach land, the Elves begin taking inventory of their supplies.
# One important consideration is food - in particular.
# The number of Calories each Elf is carrying (your puzzle input).

# The Elves take turns writing down the number of Calories contained
# by the various meals, snacks, rations, etc. that they've brought with them, one item per line.
# Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

# For example, suppose the Elves finish writing their items' Calories
# and end up with the following list:

# 1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000

# This list represents the Calories of the food carried by five Elves:

#     The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
#     The second Elf is carrying one food item with 4000 Calories.
#     The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
#     The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
#     The fifth Elf is carrying one food item with 10000 Calories.

# In case the Elves get hungry and need extra snacks, they need to know which Elf to ask:
# they'd like to know how many Calories are being carried by the Elf carrying the most Calories.
# In the example above, this is 24000 (carried by the fourth Elf).

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

def extract_elf_calorie_data(file:str) -> list:
    """extracts the list of numbers from the file"""
    elf_calorie_data = []
    with open(file, 'r', encoding='utf-8') as data_file:
        for line in data_file:
            elf_calorie_data.append(line.replace("\n", ""))
        return elf_calorie_data

extracted_data = extract_elf_calorie_data(file="./day 1/day1_puzzle1_data.txt")

def clean_elf_calorie_data(extracted_values:list) -> list:
    """clean blanks with None values for the file extract"""
    for i, item in enumerate(extracted_values):
        if item == "":
            extracted_values[i] = None
        elif isinstance(extracted_values[i], str):
            extracted_values[i] = int(extracted_values[i])
    return extracted_values

cleaned_data = clean_elf_calorie_data(extracted_values=extracted_data)

def build_elves_calorie_sums_list(clean_list:list) -> list:
    """build individual elves calorie sums"""
    num = 0
    individual_elves_calorie_sums = []
    for calories in clean_list:
        if calories is None:
            individual_elves_calorie_sums.append(num)
            num = 0
        else:
            num += calories
    return individual_elves_calorie_sums

elves_calorie_sums = build_elves_calorie_sums_list(clean_list=cleaned_data)

def find_max(numbers:list) -> int:
    """find elf with max value of calories"""
    elf_with_max_calories = max(numbers)
    return elf_with_max_calories

maximum_num = find_max(numbers=elves_calorie_sums)

print(maximum_num)
