from collections import Counter
def count(s):
    return dict(Counter(s))

a = 'aba'
print(count(a))
