# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = not(y <= (not(z <= w))) and ((not(z)) <= ((not(w)) == x)) 
#                 print(x,y,z,w,int(f))
# for n in range(10000):
#     binn = bin(n)[2:]
#     if len(binn) % 2 == 0:
#         binn = binn[:len(binn)//2]+'1'+binn[len(binn)//2:]
#     if int(binn,2) >= 26:
#         print(n)
#         break
# from turtle import *
# tracer(0)
# r = 10
# screensize(100000)
# pu()
# fd(100*r)
# rt(90)
# fd(100*r)
# rt(30)
# pd()
# for i in range(10):
#     fd(30*r)
#     rt(90)
#     fd(40*r)
#     rt(90)
# pu()
# for x in range(-150,150):
#     for y in range(-150,150):
#         goto(x*r,y*r)
#         dot(3,'red')
# exitonclick()
# print(56*2*4.5/3)
# k = 0
# x = sorted('СОРНЯК')
# for x1 in x:
#     for x2 in x:
#         for x3 in x:
#             for x4 in x:
#                 for x5 in x:
#                     for x6 in x:
#                         w = x1+x2+x3+x4+x5+x6
#                         k+=1
#                         if w.count('К') <= 3 and w.count('Я') == 2:
#                             print(k)
#                             quit()
# file = 'files\\9_var7.txt'
# with open(file) as f:
#     goidas = f.readlines()
# for i in range(len(goidas)):
#     goidas[i] = [int(j) for j in goidas[i].split()]
# goidas = [sorted(i) for i in goidas]
# k = 0
# for goida in goidas:
#     if goida[3]**2 > goida[0] * goida[1] * goida[2] or (goida[1] - goida[0] == goida[2] - goida[1] == goida[3] - goida[2]):
#         k +=1
# print(k)
# from math import ceil,log2
# i = ceil(log2(10+2022))
# b = ceil(i*158 / 8)
# print(b*15360/1024)
# a = '22' + '1'*2024 + '22'
# while '2211' in a or '1112' in a:
#     a = a.replace('111','1',1)
#     if '21' in a:
#         a = a.replace('21','12',1)
#     else:
#         a = a.replace('12','1',1)
# print(a)
# from ipaddress import ip_network
# for a in range(16,25):
#     net = ip_network(f'255.211.33.160/{a}',0)
#     ip_list = []
#     for ip in net:
#         ip = bin(int(ip))[2:]
#         ip_list.append(ip)
#     if all(ip[:16].count('1') >= ip[16:].count('1') for ip in ip_list):
#         print(a)
#         print(int('11110000',2))
# x = 243**540 - 6 * 9**530 + 21 * 3**511-3 * 3**70 - 200
# k=0
# while x > 0 :
#     if x % 9 == 8:
#         k+=1
#     x //= 9
# print(k)
# def triangle(n,m,k):
#     return n+m > k and n+k > m and m+k > n
# def f(x,a):
#     return not((triangle(x,11,18)==(not(max(x,5)>15))) and triangle(x,a,5))
    
# for a in range(100,1,-1):
#     if all(f(x,a) for x in range(1,100 0)):
#         print(a)
#         break
# from functools import lru_cache
# from time import time
# @lru_cache
# def f(n):
#     if n < 3:
#         return 1
#     if n > 2 and n % 2 == 1:
#         return f(n-1)+f(n-2)
#     if n > 2 and n % 2 == 0:
#         x = 0
#         for i in range(1,n-1):
#             x += f(i)
#         return x
# for i in range(25):
#     x = f(i)
# start = time()
# print(f(24))
# print(time()-start)
# k = 0
# s = []
# file = 'files\\17var07.txt'
# with open(file) as f:
#     goida = f.readlines()
# goida = [i.strip() for i in goida]
# goidaint = [int(i) for i in goida]
# maxgoida = max(goidaint)
# for i in range(len(goida)-2):
#     k0 = 0
#     if goida[i][-1] == '0':
#         k0 += 1
#     if goida[i+1][-1] == '0':
#         k0 += 1
#     if goida[i+2][-1] == '0':
#         k0 += 1
#     if k0 == 1 and goidaint[i]+goidaint[i+1]+goidaint[i+2] < maxgoida:
#         k+=1
#         s.append(goidaint[i]+goidaint[i+1]+goidaint[i+2])
# print(k,max(s))
# def f(s,m):
#     if s >= 153:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(s*2,m-1),f(s+1,m-1)]
#     return any(h) if m % 2 != 0 else all(h)
# print([s for s in range(1,152) if f(s,2)])
# print([s for s in range(1,152) if not(f(s,1)) and f(s,3)])
# print([s for s in range(1,152) if not(f(s,2)) and f(s,4)])
# def f(s,e):
#     if s == e:
#         return 1
#     if s < e or s == 10:
#         return 0
#     return f(s-1,e)+f(s//2,e)
# print(f(20,1)*f(50,20))
from fnmatch import fnmatch
for i in range(2049,10**9+1,2049):
    if fnmatch(str(i),'32*21?4') and i % 2049 == 0:
        print(i,i/2049)