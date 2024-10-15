# for n in range(4,10001):
#   a = '1' + n * '2'
#   while '12' in a or '3322' in a or '2222' in a:
#     if '12' in a:
#       a = a.replace('12','33',1)
#     if '2222' in a:
#       a = a.replace('2222','1',1)
#     if '3322' in a:
#       a = a.replace('3322','21',1)
#   if sum(map(int,a)) == 218:
#     print(n)
#     break
# k = 0
# from ipaddress import ip_network
# nw = ip_network('132.108.56.118/255.255.255.240',0)
# for ip in nw:
#   ip_bin = bin(int(ip))[2:]
#   ip1 = ip_bin[:-16].count('1')
#   ip2 = ip_bin[-16:].count('1')
#   if ip2 > ip1:
#     k+=1
# print(k)
# from string import ascii_uppercase
# for x in '0123456789' + ascii_uppercase[:13]:
#   z = int(f'1{x}1{x}1{x}1{x}1',23)+int(f'20{x}24',23)+int(f'1{x}235',23)
#   if z % 22 == 0:
#     print(z/22)
# def f(x,y,a):
#   return ((4*x + y < a) or (x < y) or (22 <= x))
# for a in range(-1000,1000):
#   if all(f(x,y,a) for x in range(1000) for y in range(1000)):
#     print(a)
# from sys import setrecursionlimit
# setrecursionlimit(5555)
# def f(n):
#   if n == 1:
#     return 5
#   return 2*n + 1 + f(n-1)
# print(f(2024)-f(2022))
# k = 0
# with open('17var01.txt') as f:
#   x = f.read()
# x = x.split()
# minA = 10000000
# maxI = -1
# for i in x:
#   if i[-2:] == '25':
#     minA = min(int(i),minA)
# for i in range(len(x)-2):
#   c2 = 0
#   if len(x[i]) == 2:
#     c2 += 1
#   if len(x[i+1]) == 2:
#     c2 += 1
#   if len(x[i+2]) == 2:
#     c2 += 1
#   if c2 == 1:
#     if int(x[i])+int(x[i+1])+int(x[i+2]) < minA:
#       k+=1
#       maxI = max(int(x[i])+int(x[i+1])+int(x[i+2]),maxI)
# print(k,maxI)
# def f(s,m):
#   if s >= 202:
#     return m % 2 == 0
#   if m == 0:
#     return 0
#   h = [f(s+1,m-1),f(s+4,m-1),f(s*3,m-1)]
#   return any(h) if (m-1) % 2 == 0 else all(h)
# print([s for s in range(1,202) if f(s,2)])
# print([s for s in range(1,202) if f(s,3) and not(f(s,1))])
# print([s for s in range(1,202) if f(s,4) and not(f(s,2))])
# def f(s,e):
#   if s == e:
#     return 1
#   if s > e:
#     return 0
#   if s == 11 or s == 17:
#     return 0
#   return f(s+1,e) + f(s+4,e) + f(s*2,e)
# print(f(3,24))
k = 0
for i in range(2025,10000):
  xlist = list(range(2024,i+1))
  while len(xlist) >= 3:
    xlist1 = xlist[:-2]
    xlist1.append(xlist[-1] - xlist[-2])
    xlist = sorted(xlist1)
  if sum(map(int,xlist)) == 0:
    k+= 1
  print(i)
print(k)