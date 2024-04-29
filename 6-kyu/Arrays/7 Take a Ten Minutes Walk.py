# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    n_count = walk.count('n')
    s_count = walk.count('s')
    e_count = walk.count('e')
    w_count = walk.count('w')

    return n_count == s_count and e_count == w_count


walk = ['n','s','n','s','n','s','n','s','n','s']
print(is_valid_walk(walk))
