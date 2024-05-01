# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    count = {}
    for i in seq:
        count[i] = count.get(i, 0) + 1

    for i, j in count.items():
        if j % 2 == 1:
            return i


a = [0, 1, 0, 1, 0]
print(find_it(a))
