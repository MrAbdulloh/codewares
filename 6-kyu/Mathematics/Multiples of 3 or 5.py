def solution(number):
    if number < 0:
        return 0

    ans = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
           ans.append(i)
    return sum(ans)

print(solution(15))
