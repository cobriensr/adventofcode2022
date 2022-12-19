"""Standard Imports"""

import day6_puzzle1

# Your device's communication system is correctly detecting packets,
# but still isn't working. It looks like it also needs to look for messages.

# A start-of-message marker is just like a start-of-packet marker,
# except it consists of 14 distinct characters rather than 4.

# Here are the first positions of start-of-message markers for all of the above examples:

# mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
# nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

# How many characters need to be processed before the first start-of-message
# marker is detected?

datastream = day6_puzzle1.extract_datastream(file="./day6/day6_puzzle1_data.txt")

def find_unique_characters(data:list[str]) -> int:
    """find unique characters in buffer"""
    unique = []
    holder = []
    length = 0
    for i, letter in enumerate(data):
        for alpha in letter:
            i += 1
            unique.append(alpha)
            if len(unique) == 14:
                if day6_puzzle1.is_unique_chars(unique) is False:
                    holder.append(unique.pop(0))
                else:
                    length = len(unique) + len(holder)
    return length

STREAM = find_unique_characters(data=datastream)

print(STREAM)
