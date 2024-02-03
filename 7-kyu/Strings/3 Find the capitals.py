"""
Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.

Example (Input --> Output)
"CodEWaRs" --> [0,3,4,6]
"""


def capitals(word: str) -> list[int]:
    indices = [index for index, char in enumerate(word) if char.isupper()]
    return indices

print(capitals("CodEWaRs"))
