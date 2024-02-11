"""
Modify the spacify function so that it returns the given string with spaces inserted between each character.

spacify("hello world") # returns "h e l l o   w o r l d"
"""


def spacify(string: str) -> str:
    return ' '.join(string)

print(spacify("hello world"))