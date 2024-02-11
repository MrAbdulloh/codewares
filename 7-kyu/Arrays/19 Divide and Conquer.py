"""
Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.

Return as a number.

"""


# def div_con(x):
#     xx = 0
#     ss = 0
#     for i in x:
#         if type(i) == int:
#             xx += i
#         else:
#             ss += int(i)
#
#     return (xx - ss)

def div_con(x):
    total = 0
    for item in x:
        if isinstance(item, int):
            total += item
        else:
            total -= int(item)

    return total


print(div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]))
