for x in range(1,1000):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = 0
    f = (P) <= (((Q) and (not(A))) <= (not(P)))
    if f != 1:
        print(x)