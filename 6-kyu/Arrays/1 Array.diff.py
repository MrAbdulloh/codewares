"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""


def array_diff(a: list[int], b: list[int]) -> list[int]:
    return [x for x in a if x not in b]


    # xx= []
    # for x in a:
    #     if x not in b:
    #         xx.append(x)
    # return xx


print(array_diff([1, 2, 1], [1]))  # Output: [2]
print(array_diff([1, 2, 2, 2, 3], [2]))
