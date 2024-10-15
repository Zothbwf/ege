def F(n):
    k = 2
    if n > 1:
        k += F(n-2) + F(n//2) + 1
    return k

print(F(127))
F(127)