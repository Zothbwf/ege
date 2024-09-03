for d in range(1,5000000):
    n = 10
    s = 122
    while s//d > 0:
        s = s-d
        n = n+5
    if n == 60:
        print(d)
        break
