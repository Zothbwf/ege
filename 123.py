def conv(num,osn):
    num1 = ''
    while num >= 0:
        num1 = str(num%osn)
        num = num // osn
    return num
