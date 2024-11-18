# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = not(z <= w) or x or not(y)
#                 if f == False:
#                     print(x,y,z,w)

# r_list = []
# for n in range(10000):
#     n = n - n % 4
#     n_bin = bin(n)[2:]
#     n_bin = n_bin + str(n_bin.count('1') % 2)
#     n_bin = n_bin + str(n_bin.count('1') % 2)
#     r = int(n_bin,2)
#     if r > 100:
#         r_list.append(r)
# print(min(r_list))
# r = 10000
# from turtle import *
# begin_fill()
# for _ in range(10):
#     rt(120)
#     fd(12*r)
#     rt(60)
#     fd(12*r)
# end_fill()
# canvas = getcanvas()
# k = 0
# for x in range(-1000,1000):
#     for y in range(-1000,1000):
#         if canvas.find_overlapping(x*r,y*r,x*r,y*r) == (5,):
#             k+=1
# print(k)

# from math import floor
# print(2**floor(15625*1024*8/4000/8000))

# x = '01234'
# k = 0
# for x1 in x:
#     for x2 in x:
#         for x3 in x:
#             if int(x1) > int(x2) > int(x3):
#                 k+=1
# print(k)

# file = '9_14.txt'
# with open(file) as f:
#     goida = f.read()
# goida = goida.replace(',','.')
# goida = list(map(float,goida.split()))
# sr_ar = sum(goida)/len(goida)
# max_zn = max(goida)
# print(max_zn-sr_ar)

# from math import ceil,log2
# print(200-ceil(ceil(log2(26+26+20))*10/8))

# def check_if_simple(n):
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             return False
#     return True
# for n in range(1,1000):
#     a = '>' + '0' * 15 + '1' * n + '2' * 15
#     while '>0' in a or '>1' in a or '>2' in a:
#         if '>0' in a:
#             a = a.replace('>0','22>',1)
#         if '>1' in a:
#             a = a.replace('>1','2>',1)
#         if '>2' in a:
#             a = a.replace('>2','1>',1)
#     a = a.replace('>','')
#     sum_a = sum(map(int,a))
#     if check_if_simple(sum_a):
#         print(n)
#         break

# from ipaddress import *
# for a in range(0,256):
#     goida = True
#     net = ip_network(f'126.255.{a}.100/255.255.240.0',0)
#     for ip in net:
#         ip = f'{ip:b}'
#         if sum(map(int,ip[:16])) < sum(map(int,ip[16:])):
#             goida = False
#             break
#     if goida == True:
#         print(a)

# k=0
# x = 3 ** 2020 - 3 ** 1020 + 9 ** 800 -81
# while x > 0:
#     if x % 3 == 2:
#         k+=1
#     x //= 3
# print(k)

# def f(x,a):
#     f = (x % a != 0) <= ((x % 26 == 0) <= (x % 169 != 0))
#     return f
# for a in range(1,10000):
#     if all(f(x,a) for x in range(1,10000)):
#         print(a)

# def f(n):
#     if n == 1:
#         return 1
#     if n % 2 == 0:
#         return n + 3 * f(n-1)
#     return 2 + 2 * f(n-2)
# print(f(23))

# file = "E:\\downloads\\17var14.txt"
# with open(file) as f:
#     goida = f.readlines()
# k = 0
# min_abs = 100000
# goida = [i.strip() for i in goida]
# goida_int = [int(i) for i in goida]
# for i in range(len(goida)-1):
#     if goida[i][-1] == '7' and goida[i+1][-1] == '7':
#         k+=1
#         min_abs = min(min_abs,abs(goida_int[i] - goida_int[i+1]))
# print(k,min_abs)

# def f(a,b,m):
#     if a + b >= 118:
#         return m%2 == 0
#     if m == 0:
#         return 0
#     h = [f(a*2,b,m-1),f(a,b*2,m-1),f(a,b+2,m-1),f(a+2,b,m-1)]
#     return any(h) if (m-1) % 2 == 0 else all(h)
# print([s for s in range(1,114) if (not(f(s,3,1))) and f(s,3,3)])
# print([s for s in range(1,114) if (not(f(s,3,2))) and f(s,3,4)])


# def f(s,e):
#     if s == e:
#         return 1
#     if s < e:
#         return 0 
#     return f(s-1,e) + f(s//2,e)
# print(f(31,12)*f(12,2))

# file = "E:\\downloads\\24var13-17.txt"
# with open(file) as f:
#     goida = f.read()
# max_len = 0
# goida = goida.strip()
# for i in range(len(goida)-1):
#     for j in range(i,len(goida)-1):
#         if (goida[j] == 'Z' and (goida[j+1] == 'Z' or goida[j+1] == 'Y' or goida[j+1] == 'X')):
#             max_len = max(max_len,j-i+1+1)
#         elif (goida[j] == 'Y' and (goida[j+1] == 'Y' or goida[j+1] == 'X')):
#             max_len = max(max_len,j-i+1+1)
#         elif (goida[j] == 'X' and (goida[j+1] == 'X')):
#             max_len = max(max_len,j-i+1+1)
#         else:
#             break
# print(max_len)


# def dels(n):
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             return n // i - i
#     return 0
# goida = []
# k = 0
# for m in range(850001,10**9):
#     f = dels(m)
#     if f != 0 and f % 5 == 0:
#         goida.append([m,f])
#         k+=1
#     if k == 6:
#         break
# print(*goida)