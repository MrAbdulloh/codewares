def dont_give_me_five(start: int, end: int) -> int:
    five_list = 0
    for i in range(start, end + 1):
        if '5' not in str(i):
            five_list += 1
    return five_list


print(dont_give_me_five(1, 9))
