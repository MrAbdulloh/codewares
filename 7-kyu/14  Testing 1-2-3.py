"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
"""

from typing import List


def number(lines: List[str]) -> List[str]:
    return [f"{str(i + 1)}: {c}" for i, c in enumerate(lines)]


# def number(lines: List[str]) -> List[str]:
#     number_list = []
#     for i, v in enumerate(lines):
#         number_list.append(f"{i + 1}: {v}")
#
#     return number_list


print(number(['a', 'b', 'c', 'd']))
