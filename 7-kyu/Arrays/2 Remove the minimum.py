def remove_smallest(numbers: list[int]) -> list[int]:
    if not numbers:
        return numbers
    min_index = numbers.index(min(numbers))
    print(numbers[:min_index] + numbers[min_index + 1:])


remove_smallest([5, 2, 3, 4, 5])
