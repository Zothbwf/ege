def DEL(n, m):
    return n % m == 0
list_A = []
B = list(range(70,90))
for A in range(1,1000):
    flag = True
    for x in range(1,1000):
        if (DEL(x, A) or ((x in B) <= (not(DEL(x, 22))))) == False:
                flag = False
                break
    if flag:
      list_A.append(A)
print(max(list_A))
