# for n in range(1,100000):
#     nbin = bin(n)[2:]
#     nbin = nbin[:-1]
#     if n % 2 == 0:
#         nbin = nbin + '01'
#     else:
#         nbin = nbin + '10'
#     r = int(nbin,2)
#     if r == 3022:
#         print(n)
#         break
for n in range(0,256):
    nbin = bin(n)[2:].zfill(8)
    nbinrev = ''
    for i in nbin:
        if i == '0':
            nbinrev = nbinrev + '1'
        else:
            nbinrev = nbinrev + '0'
    if (n - int(nbinrev,2)) == 131:
        print(n)
# rlist = []
# for n in range(1000):
#     nbin = bin(n)[2:]
#     nbin = nbin + str(nbin.count('1')%2)
#     nbin = nbin + str(nbin.count('1')%2)
#     r = int(nbin,2)
#     if r > 99:
#         rlist.append(r)
# print(min(rlist))
# for n in range(10000):
#     nbin = bin(n)[2:]
#     if n % 2 == 0:
#         nbin = nbin + '00'
#     else:
#         nbin = nbin + '11'
#     r = int(nbin,2)
#     if r > 215:
#         print(n)
#         break
# for n in range(1000):
#     nbin = bin(n)[2:]
#     nbin = nbin + str(nbin.count('1')%2)
#     nbin = nbin + str(nbin.count('1')%2)
#     if int(nbin,2) > 177:
#         print(n)
#         break
# rlist = []
# for n in range(1000):
#     nbin = bin(n)[2:]
#     nbin = nbin + str(nbin.count('1')%2)
#     nbin = nbin + str(nbin.count('1')%2)
#     r = int(nbin,2)
#     if r > 411:
#         rlist.append(r)
# print(min(rlist))
# rlist = []
# for n in range(1000):
#     nbin = bin(n)[2:]
#     if n % 2 == 0:
#         nbin = '1' + nbin + '0'
#     else:
#         nbin = '11' + nbin + '11'
#     r = int(nbin,2)
#     if r > 192:
#         rlist.append(r)
# print(min(rlist))
# for n in range(10000):
#     nbin = bin(n)[2:]
#     if n % 2 == 0:
#         nbin = '10' + nbin
#     else:
#         nbin = '1' + nbin + '01'
#     r = int(nbin,2)
#     if r > 541:
#         print(n)
#         break
# for n in range(10000):
#     nbin = bin(n)[2:]
#     if n % 2 == 0:
#         nbin = '10' + nbin
#     else:
#         nbin = '1' + nbin + '01'
#     r = int(nbin,2)
#     if r > 109:
#         print(n)
#         break
# for n in range(1000):
#     nbin = bin(n)[2:]
#     x = nbin.count('1')
#     if x % 2 == 0:
#         nbin = nbin + '0'
#         nbin = '10' + nbin[2:]
#     else:
#         nbin = nbin + '1'
#         nbin = '11' + nbin[2:]
#     r = int(nbin,2)
#     if r > 35:
#         print(n)
#         break