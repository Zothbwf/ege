# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = ((x == (not(y))) or (x == (not(z)))) and w and (y <= z)
#                 if f:
#                     print(x,y,z,w)


# rlist = []
# for n in range(1000):
#     n1 = n - n%8 + n%2
#     nbin = f'{n1:b}'
#     nbin = nbin + str(nbin.count('1')%2)
#     nbin = nbin + str(nbin.count('1')%2)
#     r = int(nbin,2)
#     if r > 90:
#         rlist.append(r)
# print(min(rlist))


# from turtle import * 
# r = 100000
# tracer(0)
# begin_fill()
# rt(60)
# for _ in range(4):
#     fd(8*r)
#     rt(120)
#     fd(4*r)
#     rt(240)
# rt(120)
# fd(2*r)
# rt(90)
# fd(16*r*3**0.5)
# rt(90)
# fd(2*r)
# end_fill()
# canvas = getcanvas()
# k = 0
# for x in range(-400,400):
#     for y in range(-400,400):
#         if canvas.find_overlapping(x*r,y*r,x*r,y*r) == (5,):
#             k+=1
# exitonclick()
# print(k)

# from math import floor
# print(2**floor((550*1024*8/880/1600)))

# k = 0
# x = '01234567'
# for x1 in x[1:]:
#     for x2 in x:
#         for x3 in x:
#             for x4 in x:
#                 w = x1 + x2 + x3 + x4
#                 for i in x:
#                     if i*2 in w:
#                         k+=1
#                         break
# print(k)

# f = '9_var17.txt'
# with open(f) as file:
#     goida = file.read()
# goida = goida.replace(',','.')
# goida = [float(i) for i in goida.split()]
# print(max(goida) - min(goida))

# from math import log2, floor, ceil
# print(10-ceil(7*ceil(log2(26))/8))

# a = '1' + '5' * 25 
# while '15' in a or '1' in a:
#     if '15' in a:
#         a = a.replace('15','5551',1)
#     elif '1' in a:
#         a = a.replace('1','5',1)
# print(a.count('5'))


# from ipaddress import ip_network,ip_address
# find = ip_address('244.55.138.96')
# for a in range(6,33):
#     net = ip_network(f'244.55.138.100/{a}',0)
#     if find in net:
#         print(a)

# for x in '0123456789ABCDE':
#     goida = int(f'135{x}7',15) + int(f'7{x}531',15)
#     if goida % 14 == 0:
#         print(goida / 14)
        
# def f(x,y,a):
#     f = (x >= a) or (y >= a) or (x*y <= 200)
#     return f
# for a in range(0,1000):
#     if all(f(x,y,a) == True for x in range(1,1000) for y in range(1,1000)):
#         print(a)

# def f(n):
#     if n == 1:
#         return 1
#     return n * f(n-1)
# print(f(446)/f(443))

# file = "E:\\downloads\\17var17.txt"
# k = 0
# max_product = float('-inf')
# with open(file) as f:
#     goida = f.readlines()
# goida = [i.strip() for i in goida]
# zov = [int(i) for i in goida]
# for i in range(len(zov)-1):
#     sum_two = zov[i] + zov[i+1]
#     if (zov[i] < 0 or zov[i+1] < 0) and sum_two >= 100:
#         k+=1
#         max_product = max(max_product,zov[i]*zov[i+1])
# print(k,max_product)

# def f(a,b,m):
#     if a+b >= 101:
#         return m%2 == 0
#     if m == 0:
#         return 0
#     h = [f(a+1,b,m-1),f(a*2,b,m-1),f(a,b+1,m-1),f(a,b*2,m-1)]
#     return any(h) if (m-1) % 2 == 0 else all(h)
# print([a for a in range(1,94) if f(a,7,3) and not(f(a,7,1))])
# print([a for a in range(1,94) if f(a,7,4) and not(f(a,7,2))])

# def f(s,e):
#     if s > e:
#         return 0
#     if s == e:
#         return 1
#     return f(s+2,e) + f(s*2,e) + f(s*3,e)
# print(f(1,6)*f(6,24))

# file = "E:\\downloads\\24var13-17 (1).txt"
# lens = []
# with open(file) as f:
#     goida = f.read()
# goida = goida.strip()
# goida = goida.split('Z')
# lens = [len(i) for i in goida]
# par = []
# for i in range(len(lens)-2):
#     par.append(lens[i]+lens[i+1]+lens[i+2]-1)
# print(max(par))
