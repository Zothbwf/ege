file = 'files\\17_17873.txt'
k = 0
maxSumm = -1
with open(file) as f:
    x = f.read()
listX = x.split()
intX = [int(i) for i in listX]
for i in range(len(intX)-1):
    if intX[i] % 16 == min(intX) or intX[i+1] % 16 == min(intX):
        k += 1
        summ = intX[i] + intX[i+1]
        if summ > maxSumm:
            maxSumm = summ
            
print(k,maxSumm)