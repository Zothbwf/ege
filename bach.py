answers = {
    '1':'35',
    '2':'xwyz',
    '3':'6050',
    '4':'13',
    '5':'63',
    '7':'37'
}
from itertools import product
"""
print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (y <= x) and not(w) and z
                if f:
                    print(w,x,y,z)
"""
"""
rlist = []
for N in range(1,3000):
    Nbin = bin(N)[2:]
    if Nbin.count('1') % 2 == 0:
        Nbin = Nbin + '11'
    else:
        Nbin = Nbin + '01'
    r = int(Nbin,2)
    if r > 61:
        rlist.append(r)
print(min(rlist))
"""
"""
print(16*1000*51*26*2*60/(2**26))
"""
"""
c = 0
for x in x:
    c = c + 1
    if x.count('Ь') == 0 and x[0] == 'Р' and c % 2 == 0:
        print(c,x)
"""
c = 0
import ipaddress
huita = ipaddress.ip_network(f'228.172.236.0/255.255.240.0',0)
for ip in huita:
    ip_2 = bin(int(ip))[2:].zfill(32)
    if ip_2.count('1') % 5 != 0:
        c += 1
print(c)
print(170+33*5+26*5+30*5)