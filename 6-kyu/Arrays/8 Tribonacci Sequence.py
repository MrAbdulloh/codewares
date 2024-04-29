def tribonacci(signature, n):
    dup_signature = signature.copy()

    for _ in range(n - 3):
        next_number = sum(dup_signature[-3:])
        dup_signature.append(next_number)
    return dup_signature[:n]


signature = [1, 1, 1]
n = 1
print(tribonacci(signature, n))
