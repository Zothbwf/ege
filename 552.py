listN = list()
for n in range(10000):
    binN = bin(n)[2:]
    if binN.count('1')>binN.count('0'):
        binN = binN + '1'
    else:
        binN = binN + '0'
    if int(binN,2) > 36:
        listN.append(int(binN,2))
print(min(listN))