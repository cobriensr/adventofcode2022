"""Standard Imports"""

import day5_puzzle1

# As you watch the crane operator expertly rearrange the crates,
# you notice the process isn't following your prediction.

# Some mud was covering the writing on the side of the crane,
# and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

# The CrateMover 9001 is notable for many new and exciting features:
# air conditioning, leather seats, an extra cup holder,
# and the ability to pick up and move multiple crates at once.

# Again considering the example above, the crates begin in the same configuration:

#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

# Moving a single crate from stack 2 to stack 1 behaves the same as before:

# [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

# However, the action of moving three crates from stack 1 to stack 3
# means that those three moved crates stay in the same order,
# resulting in this new configuration:

#         [D]
#         [N]
#     [C] [Z]
#     [M] [P]
#  1   2   3

# Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

#         [D]
#         [N]
# [C]     [Z]
# [M]     [P]
#  1   2   3

# Finally, a single crate is still moved from stack 1 to stack 2,
# but now it's crate C that gets moved:

#         [D]
#         [N]
#         [Z]
# [M] [C] [P]
#  1   2   3

# In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

# Before the rearrangement process finishes, update your simulation so that the Elves know
# where they should stand to be ready to unload the final supplies.
# After the rearrangement procedure completes, what crate ends up on top of each stack?

# build out columns of stacks of crates
stack1 = ['N', 'D', 'M', 'Q', 'B', 'P', 'Z']
stack2 = ['C', 'L', 'Z', 'Q', 'M', 'D', 'H', 'V']
stack3 = ['Q', 'H', 'R', 'D', 'V', 'F', 'Z', 'G']
stack4 = ['H', 'G', 'D', 'F', 'N']
stack5 = ['N', 'F', 'Q']
stack6 = ['D', 'Q', 'V', 'Z', 'F', 'B','T']
stack7 = ['Q', 'M', 'T', 'Z', 'D', 'V', 'S', 'H']
stack8 = ['M', 'G', 'F', 'P', 'N', 'Q']
stack9 = ['B', 'W', 'R', 'M']

# map stacks to iterator
stacks = {
            1 : stack1,
            2 : stack2,
            3 : stack3,
            4 : stack4,
            5 : stack5,
            6 : stack6,
            7 : stack7,
            8 : stack8,
            9 : stack9
}

# extract crate movements from list of movements
crates = day5_puzzle1.extract_crate_assignments(file="./day5/day5_puzzle1_data.txt")

def move_all_crates(move_list: list[list[int]]):
    """move crates through the list of crate moves"""
    moves = 0
    removals = []
    for item in move_list:
        for i, element in enumerate(item):
            if i == 0:
                moves = element
            elif i == 1:
                start = len(stacks[element]) - moves
                removals.append(stacks[element][start:])
                del stacks[element][start:]
            elif i == 2:
                stacks[element].extend(removals[0])
                removals = []

def find_top_crates() -> str:
    """find the top create in each stack"""
    move_all_crates(move_list=crates)
    top_crates = []
    top_list = ''
    for i, item in enumerate(stacks):
        top_crates.append(stacks[item].pop())
    top_list = top_list.join(top_crates)
    return top_list

OUTPUT = find_top_crates()

print(OUTPUT)
