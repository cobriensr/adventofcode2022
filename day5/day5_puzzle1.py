"""Standard imports"""

# The expedition can depart as soon as the final supplies have been unloaded from the ships.
# Supplies are stored in stacks of marked crates,
# but because the needed supplies are buried under many other crates,
# the crates need to be rearranged.

# The ship has a giant cargo crane capable of moving crates between stacks.
# To ensure none of the crates get crushed or fall over,
# the crane operator will rearrange them in a series of carefully-planned steps.
# After the crates are rearranged,
# the desired crates will be at the top of each stack.

# The Elves don't want to interrupt the crane operator during this delicate procedure,
# but they forgot to ask her which crate will end up where,
# and they want to be ready to unload them as soon as possible so they can embark.

# They do, however,
# have a drawing of the starting stacks of crates and the rearrangement procedure
# (your puzzle input).For example:

#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# In this example, there are three stacks of crates.
# Stack 1 contains two crates: crate Z is on the bottom,
# and crate N is on top. Stack 2 contains three crates; from bottom to top,
# they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

# Then, the rearrangement procedure is given. In each step of the procedure,
# a quantity of crates is moved from one stack to a different stack.
# In the first step of the above rearrangement procedure,
# one crate is moved from stack 2 to stack 1, resulting in this configuration:

# [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
# In the second step, three crates are moved from stack 1 to stack 3.
# Crates are moved one at a time, so the first crate to be moved (D)
# ends up below the second and third crates:

#         [Z]
#         [N]
#     [C] [D]
#     [M] [P]
#  1   2   3
# Then, both crates are moved from stack 2 to stack 1.
# Again, because crates are moved one at a time, crate C ends up below crate M:

#         [Z]
#         [N]
# [M]     [D]
# [C]     [P]
#  1   2   3
# Finally, one crate is moved from stack 1 to stack 2:

#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3
# The Elves just need to know which crate will end up on top of each stack;
# in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3,
# so you should combine these together and give the Elves the message CMZ.

# After the rearrangement procedure completes, what crate ends up on top of each stack?

#     [V] [G]             [H]
# [Z] [H] [Z]         [T] [S]
# [P] [D] [F]         [B] [V] [Q]
# [B] [M] [V] [N]     [F] [D] [N]
# [Q] [Q] [D] [F]     [Z] [Z] [P] [M]
# [M] [Z] [R] [D] [Q] [V] [T] [F] [R]
# [D] [L] [H] [G] [F] [Q] [M] [G] [W]
# [N] [C] [Q] [H] [N] [D] [Q] [M] [B]
#  1   2   3   4   5   6   7   8   9

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

def extract_crate_assignments(file:str) -> list[int]:
    """extracts the movements from the list of movements"""
    crate_list = []
    with open(file, 'r', encoding='utf-8') as data_file:
        for line in data_file:
            movements = line.strip().split(" ")
            movements.remove('move')
            movements.remove('from')
            movements.remove('to')
            movements = [int(i) for i in movements]
            crate_list.append(movements)
        return crate_list

crates = extract_crate_assignments(file="./day5/day5_puzzle1_data.txt")

def move_crates(move_list: list[list[int]]):
    """move crates through the list of crate moves"""
    moves = 0
    removals = []
    for item in move_list:
        for i, element in enumerate(item):
            if i == 0:
                moves = element
            elif i == 1:
                for j in range(1, moves+1, 1):
                    removals.append(stacks[element].pop())
            elif i == 2:
                stacks[element].extend(removals)
                removals = []

def find_top_crates() -> str:
    """find the top create in each stack"""
    move_crates(move_list=crates)
    top_crates = []
    top_list = ''
    for i, item in enumerate(stacks):
        top_crates.append(stacks[item].pop())
    top_list = top_list.join(top_crates)
    return top_list

OUTPUT = find_top_crates()

print(OUTPUT)
