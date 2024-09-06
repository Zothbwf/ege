count = 0
with open('files/9_17672.txt') as den:
    for line in den.readlines()[:-1]:
        a = [int(i) for i in line.split()]
        a = sorted(a)

        if a[0]+a[3] < a[1] + a[2]:
            count +=1
print(count)