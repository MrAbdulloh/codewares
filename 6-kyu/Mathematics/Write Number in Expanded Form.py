def expanded_form(num):
    str_num, i = str(num).split('.')

    str_len = len(str_num)  # 3
    result = []
    for index, digit in enumerate(str_num):
        if digit != '0':
            add = digit + '0' * (str_len - index - 1)
            result.append(add)
    # return ' + '.join(result)
    i_len = len(i)
    result_i = []
    for ix , dx in enumerate(i):
        if dx != '0':
            add = dx + '0' * (i_len - ix)
            result_i.append(add)
    return result_i

print(expanded_form(807.304))
