file = "E:\\downloads\\17_2.txt"
max_sum = -9999999
k = 0
with open(file) as f:
    goida = f.readlines()
goida = [i.strip() for i in goida]
zov = [int(i) for i in goida]
max_13 = max([int(i) for i in goida if i[-2:] == '13'])
for i in range(len(goida)-2):
    lens = [len(j) for j in goida[i:i+3]]
    if lens.count(3) == 2 and (zov[i]+zov[i+1]+zov[i+2]) < max_13:
        k+=1
        max_sum = max(max_sum,zov[i]+zov[i+1]+zov[i+2])
print(k,max_sum)