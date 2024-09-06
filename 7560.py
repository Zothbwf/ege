A_list = []
for A in range(1,1000):
    flag = True
    for x in range(1,400):
        for y in range(1,400 ):
            if ((x + y <= 30) or (y <= x + 2) or (y >= A)) == False:
                flag = False
                break
    if flag:
      A_list.append(A)
print(max(A_list))
