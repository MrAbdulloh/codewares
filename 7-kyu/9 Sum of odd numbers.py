def triangle_sum(n):
    if n == 1:
        return 1
    else:
        first_number = (n - 1) * 2 + 1
        return first_number + sum(range(first_number + 2, first_number + 2 * n, 2))
