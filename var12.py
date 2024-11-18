# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((x <= y) <= w) or (z <= (y and w))) == 0:
#                     print(x,y,z,w)

# for n in range(100,1000):
#     razr_n = [int(i) for i in str(n)]
#     sum_n = sum(razr_n)
#     mnozh_n = razr_n[0] * razr_n[1] * razr_n[2]
#     ans = sorted([sum_n,mnozh_n],reverse=True)
#     ans = str(ans[0]) + str(ans[1])
#     if int(ans) == 24019:
#         print(n)

# from turtle import *
# r = 10000
# lt(90)
# tracer(0)
# pd()
# begin_fill()
# for i in range(18):
#     fd(19*r)
#     rt(60)
# pu()
# end_fill()
# canvas = getcanvas()
# cnt = 0
# for x in range(-40,40):
#     for y in range(-40,40):
#        if canvas.find_overlapping(x*r,y*r,x*r,y*r,) == (5,):
#            cnt +=1
# print(cnt)
# exitonclick()

# print(2**int((35*1024*8/(112*240))))

# x = sorted('ВАЛИК')
# k = 0
# for x1 in x:
#     for x2 in x:
#         for x3 in x:
#             for x4 in x:
#                 for x5 in x:
#                     for x6 in x:
#                         w = x1+x2+x3+x4+x5+x6
#                         k += 1
#                         if w.count('А') <= 2 and w.count('В') == 2 and w.count('И') == 0:
#                             print(k)
#                             exit()

# file = '9_var12.txt'
# with open(file) as f:
#     a = f.read()
# a = a.replace(',','.')
# concentrations = [float(i) for i in a.split()]
# concentrations = sorted(concentrations)
# print(concentrations)
# uniq_concetrations = sorted(list(set(concentrations)))
# min3 = uniq_concetrations[:3]
# max3 = uniq_concetrations[-3:]
# k = 0
# for i in concentrations:
#     if i in min3 or i in max3:
#         continue
#     k+= 1
# print(k)

# from math import log2,ceil
# bit = ceil(log2(26+2020))
# byte = ceil(98*bit/8)
# ans = 13312 * byte / 1024
# print(ans)

# a = '1' * 65
# while '11111' in a or '15' in a:
#     if '11111' in a:
#         a = a.replace('11111','15',1)
#     else:
#         a = a.replace('15','1',1)
# print(a)

# from ipaddress import *
# for a in range(0,256):
#     goida = True
#     net = ip_network(f'64.129.{a}.10/255.255.252.0',0)
#     for ip in net:
#         ip = bin(int(ip))[2:]
#         if ip[:16].count('1') > ip[16:].count('1'):
#             goida = False
#     if goida:
#         print(a)
#         break

# x = 3**2021 + 5 * 3**2000 + 3**501 + 5 * 3**500 + 1
# k = 0
# while x > 0:
#     if x % 9 == 0:
#         k+= 1
#     x //= 9
# print(k)

# from itertools import combinations
# def f(x,a1,a2):
#     b = (4 <= x <=18)
#     c = (12 <= x <= 40)
#     a = (a1 <= x <= a2)
#     f = (not(a)) <= (b == c)
#     return f
# lens = []
# ox = [i/4 for i in range(1*4,50*4)]
# for a1,a2 in combinations(ox,2):
#     if all(f(x,a1,a2) for x in range(-100,100)):
#         lens.append(a2-a1)
# print(min(lens))

# from functools import lru_cache
# @lru_cache()
# def f(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return n * (n-1) + f(n-1) + f(n-2)
# for i in range(1,2200):
#     goida = f(i)
# print(f(2023)-f(2021)-2*f(2020)-f(2019))

# k = 0
# sums = []
# file = '17var12.txt'
# with open(file) as f:
#     goida = f.readlines()
# goida_int = [int(i.strip()) for i in goida]
# for i in range(len(goida_int)-1):
#     if goida_int[i] % 5 == 0 and goida_int[i+1] % 5 == 0:
#         k+=1
#         sums.append(goida_int[i] + goida_int[i+1])
# print(k,min(sums))

# def f(s,m):
#     if s >= 2022:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(s*2,m-1),f(s+1,m-1)]
#     return any(h) if (m-1) % 2 == 0 else all(h)
# print(19,*[s for s in range(1,2021) if f(s,2)])
# print(20,*[s for s in range(1,2021) if f(s,3) and not(f(s,1))])
# print(*[s for s in range(1,2021) if f(s,4) and not(f(s,2))])

# def f(s,e):
#     if s == e:
#         return 1
#     if s > e:
#         return 0
#     return f(s+2,e) + f(s+10,e)
# print(f(7,71))

# file = '24var09-12.txt'
# with open(file) as f:
#     goida = f.read()
# while '12' in goida:
#     goida = goida.replace('12','1 2')
# while '13' in goida:
#     goida = goida.replace('13','1 3')
# while '21' in goida:
#     goida = goida.replace('21','2 1')
# while '31' in goida:
#     goida = goida.replace('31','3 1')
# goida = goida.split()
# goida_lens = [len(i) for i in goida]
# print(max(goida_lens))



# k = 0
# def dels(n):
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             return n // i - i
#     return 0
# for i in range(800000-1,0,-1):
#     m = dels(i)
#     if m and m % 23 == 0:
#         print(i,m)
#         k+=1
#     if k == 5:
#         exit()

