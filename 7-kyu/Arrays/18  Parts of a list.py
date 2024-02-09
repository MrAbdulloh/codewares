def partlist(arr):
    result = []
    for i in range(1, len(arr)):
        part1 = ' '.join(arr[:i])
        part2 = ' '.join(arr[i:])
        result.append((part1, part2))
    return result

a = ["az", "toto", "picaro", "zone", "kiwi"]
print(partlist(a))