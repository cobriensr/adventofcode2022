"""Standard imports"""

import day4_puzzle1

# It seems like there is still quite a bit of duplicate work planned.
# Instead, the Elves would like to know the number of pairs that overlap at all.

# In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap,
# while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

# 5-7,7-9 overlaps in a single section, 7.
# 2-8,3-7 overlaps all of the sections 3 through 7.
# 6-6,4-6 overlaps in a single section, 6.
# 2-6,4-8 overlaps in sections 4, 5, and 6.

# So, in this example, the number of overlapping assignment pairs is 4.

# In how many assignment pairs do the ranges overlap?

assignments = day4_puzzle1.extract_cleaning_assignments(file="./day4/day4_puzzle2_data.txt")

written = day4_puzzle1.write_assignments(assignments)

def build_ranges(range_list: list) -> int:
    """build ranges for each assignment"""
    counter = 0
    for item in range_list:
        path_1 = list(range(int(item[0][0]), int(item[0][1])+1))
        path_2 = list(range(int(item[1][0]), int(item[1][1])+1))
        result_1 = any(elem in path_1 for elem in path_2)
        result_2 = any(elem in path_2 for elem in path_1)
        if result_1 or result_2 is True:
            counter += 1
    return counter

BUILT = build_ranges(range_list=written)

print(BUILT)
