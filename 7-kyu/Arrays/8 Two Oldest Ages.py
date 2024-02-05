def two_oldest_ages(ages: list[int]) -> list[int]:
    return [sorted(ages)[-2], sorted(ages)[-1]]
