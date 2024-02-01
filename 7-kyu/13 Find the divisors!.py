from typing import List


def divisors(integer: int) -> List[int]:
    list_divisors = []
    for divisor in range(2, integer):
        if integer % divisor == 0:
            list_divisors.append(divisor)

    if not list_divisors:
        return f"{integer} is prime"
    return list_divisors


print(divisors(100))
