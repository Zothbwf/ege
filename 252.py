def sysChils(num,osn):
    num_in_chils = ''
    while num > 0:
        num_in_chils = str(num%osn) + num_in_chils 
        num = num//osn
    return num_in_chils
for osn in range(2,52):
    if sysChils(79,osn)[-1] == '2' and sysChils(111,osn)[-1] == '1':
        print(osn)