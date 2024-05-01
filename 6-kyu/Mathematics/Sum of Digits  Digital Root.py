def digital_root(n):
    str_n = str(n)
    if len(str_n) == 1:
        return n

    ans = sum([int(i) for i in str_n])

    return digital_root(ans)


print(digital_root(942))
