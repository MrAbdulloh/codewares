def min_max(lst: list[int]) -> list[int]:
    list_min = min(lst)
    list_max = max(lst)
    return [list_min, list_max]

print(min_max([]))