def highest_rank(arr):
    return max(arr, key=lambda x: (arr.count(x), x))


arr = [1, 1, 2, 3]
print(highest_rank(arr))
