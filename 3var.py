# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (not(x <= y) or ((not w) <= (not z)) or w) == 0 :
#                     print(x,y,z,w)
# def s(n,o):
#     x = ''
#     while n > 0:
#         x = str(n%o) + x
#         n = n // o
#     return x
# for n in range(1,10000):
#     n4 = s(n,4)
#     if n % 4 == 0:
#         n4 = n4 + n4[-2:]
#     else:
#         ost = n%4
#         ost *= 2
#         n4 = n4 + s(ost,4)
#     if int(n4,4) >= 1025:
#         print(n)
#         break

# from turtle import *
# r = 10
# tracer(0)
# screensize(10000,10000)
# for _ in range(3):
#     pd()
#     for _ in range(2):
#         fd(10*r)
#         rt(90)
#         fd(10*r)
#         rt(90)
#     pu()
#     fd(5*r)
#     rt(90)
#     fd(5*r)
#     lt(90)
# pu()
# for x in range(-40,40):
#     for y in range(-40,40):
#         goto(x*r,y*r)
#         dot(3,'red')
# update()
# exitonclick()

# print(24*96000*2*10/28800)
# k = 0
# c = 0
# x = sorted('ФЛАМИНГО')
# for z1 in x:
#     for z2 in x:
#         for z3 in x:
#             for z4 in x:
#                 for z5 in x:
#                     w = z1 + z2 + z3 +z4 + z5
#                     k+=1
#                     if w[0] != 'Н' and w.count('О') <= 1 and k % 2 != 0:
#                         c += 1
# print(c)
# k = 0
# with open('files//9_VAR3.txt') as f:
#     x = f.readlines()
# for goida in x:
#     goida = [int(i) for i in goida.split()]
#     povt3 = [i for i in goida if goida.count(i) == 3]
#     povt2 = [i for i in goida if goida.count(i) == 2]
#     npov = [i for i in goida if goida.count(i) == 1]
#     sr_npov = sum(npov) / len(npov)
#     if len(povt3) == 3 and len(povt2) == 2 and len(npov) == 3 and  sr_npov <= povt3[0]:
#         k+=1
# print(k)

# from math import log2
# print(454*3072/1024)

# for n in range(3,10001):
#     a = '4' + '1' * n
#     while '31' in a or '411' in a or '1111' in a:
#         if '31' in a:
#             a = a.replace('31','1',1)
#         if '411' in a:
#             a = a.replace('411','13',1)
#         if '1111' in a:
#             a = a.replace('1111','4',1)
#     s = sum(map(int,a))
#     if s == 36:
#         print(n)
#         break

# from ipaddress import *
# k = 0
# net = ip_network('23.140.159.160/255.255.252.0',0)
# for ip in net:
#     binip =  bin(int(ip))[2:]
#     ip1 = binip[:-16].count('1')
#     ip2 = binip[-16:].count('1')
#     if ip1 >= ip2:
#         k+=1
#     print(k)
# from string import ascii_uppercase
# alp = '0123456789' + ascii_uppercase[:15]
# for x in alp:
#     i = int(f'1{x}2{x}3{x}4{x}5',25) + int(f'2{x}024',25) + int(f'1{x}099',25)
#     if i % 24 == 0:
#         print(i/24) 

# def f(x,y,a):
#     return (  (x<4) or (x >= 20) or (y >= 3*x + a) or (y< 100) )
# for a in range(1000):
#     if all(f(x,y,a) for x in range(0,1000) for y in range(0,1000)):
#         print(a)
# from sys import setrecursionlimit
# from functools import lru_cache
# @lru_cache()
# def f(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return n * (n-1) + f(n-1) + f(n-2)
# for i in range(1,2025):
#     x = f(i)
# print(f(2024) - f(2022) - 2 * f(2021) - f(2020))
# a = []
# b = []
# with open('files/17var03.txt') as f:
#     l = f.read()
# for i in l.split():
#     if i[-2:] == '90':
#         a.append(int(i))
# maxA = (max(a))
# l = l.split()
# lint = [int(i) for i in l]
# for i in range(len(l)-2):
#     if lint[i] + lint[i+1] + lint[i+2] > maxA and (len(l[i]) == 4 or len(l[i+1]) == 4 or len(l[i+2]) == 4):
#         b.append((lint[i] + lint[i+1] + lint[i+2]))
# print(len(b),min(b))

# def f(s,m):
#   if s >= 205:
#     return m % 2 == 0
#   if m == 0:
#     return 0
#   h = [f(s+1,m-1),f(s+5,m-1),f(s*4,m-1)]
#   return any(h) if (m-1) % 2 == 0 else all(h)
# print([s for s in range(1,204) if f(s,2)])
# print([s for s in range(1,204) if f(s,3) and not(f(s,1))])
# print([s for s in range(1,204) if f(s,4) and not(f(s,2))])

def f(s,e):
    if s == e:
        return 1
    if s > e or s == 6 or s == 17:
        return 0
    return f(s+2,e) + f(s+3,e) + f(s*5,e)
print(f(1,31))