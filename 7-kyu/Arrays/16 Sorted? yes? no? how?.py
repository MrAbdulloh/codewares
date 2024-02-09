def is_sorted_and_how(arr):
    sortdesc = sorted(arr, reverse=True)
    if arr == sorted(arr):
        return 'yes, ascending'
    elif arr == sortdesc:
        return "yes, descending"
    else:
        return "no"


# 2 method
# def is_sorted_and_how(arr):
#     ascending = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
#     descending = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
#
#     if ascending:
#         return 'yes, ascending'
#     elif descending:
#         return 'yes, descending'
#     else:
#         return 'no'

print(is_sorted_and_how([15, 7, 3, -8, 19, ]))
