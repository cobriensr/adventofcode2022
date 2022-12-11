"""Standard imports"""

# One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey
# Unfortunately, that Elf didn't quite follow the packing instructions,
# and so a few items now need to be rearranged.

# Each rucksack has two large compartments.
# All items of a given type are meant to go into exactly one of the two compartments.
# The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

# The Elves have made a list of all of the items currently in each rucksack (your puzzle input),
# but they need your help finding the errors.
# Every item type is identified by a single lowercase or uppercase letter
# (that is, a and A refer to different types of items).

# The list of items for each rucksack is given as characters all on a single line.
# A given rucksack always has the same number of items in each of its two compartments,
# so the first half of the characters represent items in the first compartment,
# while the second half of the characters represent items in the second compartment.

# For example, suppose you have the following list of contents from six rucksacks:

# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw

# The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp,
# which means its first compartment contains the items vJrwpWtwJgWr,
# while the second compartment contains the items hcsFMMfFFhFp.
# The only item type that appears in both compartments is lowercase p.
# The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL.
# The only item type that appears in both compartments is uppercase L.
# The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg;
# the only common item type is uppercase P.
# The fourth rucksack's compartments only share item type v.
# The fifth rucksack's compartments only share item type t.
# The sixth rucksack's compartments only share item type s.

# To help prioritize item rearrangement, every item type can be converted to a priority:

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# In the above example,
# the priority of the item type that appears in both compartments of each rucksack is
# 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

# Find the item type that appears in both compartments of each rucksack.
# What is the sum of the priorities of those item types?

# create dictionary of letter priorities

letter_priority = {
                    "a" : 1,
                    "b" : 2,
                    "c" : 3,
                    "d" : 4,
                    "e" : 5,
                    "f" : 6,
                    "g" : 7,
                    "h" : 8,
                    "i" : 9,
                    "j" : 10,
                    "k" : 11,
                    "l" : 12,
                    "m" : 13,
                    "n" : 14,
                    "o" : 15,
                    "p" : 16,
                    "q" : 17,
                    "r" : 18,
                    "s" : 19,
                    "t" : 20,
                    "u" : 21,
                    "v" : 22,
                    "w" : 23,
                    "x" : 24,
                    "y" : 25,
                    "z" : 26,
                    "A" : 27,
                    "B" : 28,
                    "C" : 29,
                    "D" : 30,
                    "E" : 31,
                    "F" : 32,
                    "G" : 33,
                    "H" : 34,
                    "I" : 35,
                    "J" : 36,
                    "K" : 37,
                    "L" : 38,
                    "M" : 39,
                    "N" : 40,
                    "O" : 41,
                    "P" : 42,
                    "Q" : 43,
                    "R" : 44,
                    "S" : 45,
                    "T" : 46,
                    "U" : 47,
                    "V" : 48,
                    "W" : 49,
                    "X" : 50,
                    "Y" : 51,
                    "Z" : 52,
                }

def extract_rucksack_item_lists(file:str) -> list:
    """extracts the item lists from the rucksacks"""
    rucksack_item_list = []
    with open(file, 'r', encoding='utf-8') as data_file:
        for line in data_file:
            rucksack_item_list.append(line.replace("\n", ""))
        return rucksack_item_list

extracted_data = extract_rucksack_item_lists(file="./day3/day3_puzzle1_data.txt")

def count_str_len(items: list) -> None:
    """test that all string lengths are even"""
    for item in items:
        if len(item) % 2 != 0:
            print("not even length")

def split_item_lists(lists: list) -> list:
    """split item lists into 2 containers"""
    count_str_len(lists)
    rucksack_containers = []
    for item in lists:
        first_half = item[:len(item)//2]
        second_half = item[len(item)//2:]
        rucksack_containers.append([first_half, second_half])
    return rucksack_containers

item_lists = split_item_lists(lists=extracted_data)

def find_duplicate_items(list_of_items:list) -> list:
    """find duplicate item in each rucksack container"""
    dupes = []
    for item in list_of_items:
        for letter in item[0]:
            if letter in item[1]:
                dupes.append(letter)
                break
        else:
            continue
    return dupes

duplicates = find_duplicate_items(list_of_items=item_lists)

def map_values(dupe_list:list) -> list:
    """map values from dictionary to duplicates"""
    mapped = []
    for duplicate in dupe_list:
        mapped.append(letter_priority[duplicate])
    return mapped

values = map_values(dupe_list=duplicates)

total = sum(values)

print(total)
