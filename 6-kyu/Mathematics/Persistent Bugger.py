def persistence(n):
    ans = 0
    while n >= 10:
        result = 1
        for digit in str(n):
            result *= int(digit)
        n = result
        ans += 1
    return ans

print(persistence(39))  # Output: 3
print(persistence(999)) # Output: 4
print(persistence(4))   # Output: 0