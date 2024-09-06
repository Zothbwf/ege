count = 0
with open('files/9_17628.txt') as den:
    for line in den.readlines():
        a = [int(i) for i in line.split()]
        a.sort()
        if a[0]+a[3] <= a[2]+a[1]:
            count +=1
print(count)