def DEL(n, m):
    return n % m == 0
list_A = []
for A in range(1,1000):
    flag = True
    for x in range(1,1000):
        if (DEL(x, 33) <= ((not(DEL(x, A))) <= (not(DEL(x, 242))))) == False:
                flag = False
                break
    if flag:
      list_A.append(A)
print(max(list_A))
