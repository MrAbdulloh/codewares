def reverse_alternate(st):
    res = st.strip().split()
    for i in range(1, len(res), 2):
        res[i] = res[i][::-1]
    return ' '.join(res)



print(reverse_alternate("Did it work?"))
