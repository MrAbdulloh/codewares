def catch_sign_change(lst):
    if not lst:
        return 0

    sign_changes = 0
    current_sign = 0 if lst[0] == 0 else (1 if lst[0] > 0 else -1)

    for num in lst[1:]:
        next_sign = 0 if num == 0 else (1 if num > 0 else -1)

        if next_sign != current_sign:
            sign_changes += 1
            current_sign = next_sign

    return sign_changes

# Пример использования:
lst = [1,5,2,-4]
print(catch_sign_change(lst))  # Вывод: 2
