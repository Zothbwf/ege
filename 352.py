for n in range(10000):
    binN = bin(n)[2:]
    if n%2 == 0:
        binN = '1' + binN
    else:
        binN = binN + '1'
    if binN.count('1') % 2 == 0:
        binN = binN + '1'
    else:
        binN = binN + '0'
    if int(binN,2) > 228:
        print(n)
        break