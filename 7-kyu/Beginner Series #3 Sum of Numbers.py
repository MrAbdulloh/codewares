def get_sum(a, b):
    if a == b:
        return a

    start, end = sorted([a, b])

    result_sum = sum(range(start, end + 1))
    return result_sum


print(get_sum(-1, -14))
