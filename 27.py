from math import dist
def which_clast(coords,t):
   x,y = coords
   if t == 'a':
      if y + 3/5*x < 5:
         return 0
      else:
         return 1
   if t == 'b':
      if x > 5:
         return 2
      if y + 2*x < 8:
         return 0
      return 1
f_a = "E:\\downloads\\27_A_17882.txt"
f_b = "E:\\downloads\\27_B_17882.txt"
with open(f_a) as file_a:
   a = file_a.readlines()
for i in range(len(a)):
   a[i] = [float(j) for j in a[i].split()]
clasts = [[],[]]
for i in range(len(a)):
   clasts[which_clast(a[i],'a')].append(a[i])
centers = []
for clast in clasts:
   min_sum_dist = 10**9
   for i in range(len(clast)):
      sum_dist = 0
      for j in range(len(clast)):
         sum_dist += dist(clast[i],clast[j])
      if sum_dist < min_sum_dist:
         center = clast[i]
         min_sum_dist = sum_dist
   centers.append(center)
x_sum = 0
y_sum = 0
for center in centers:
   x_sum += center[0]
   y_sum += center[1]
x_sum *= 10000
y_sum *= 10000
x_sr = x_sum / len(centers)
y_sr = y_sum / len(centers)
print(x_sr,y_sr)

with open(f_b) as file_b:
   b = file_b.readlines()
for i in range(len(b)):
   b[i] = [float(j) for j in b[i].split()]
clasts = [[],[],[]]
for i in range(len(b)):
   clasts[which_clast(b[i],'b')].append(b[i])
centers = []
for clast in clasts:
   min_sum_dist = 10**9
   for i in range(len(clast)):
      sum_dist = 0
      for j in range(len(clast)):
         sum_dist += dist(clast[i],clast[j])
      if sum_dist < min_sum_dist:
         center = clast[i]
         min_sum_dist = sum_dist
   centers.append(center)
x_sum = 0
y_sum = 0
for center in centers:
   x_sum += center[0]
   y_sum += center[1]
x_sum *= 10000
y_sum *= 10000
x_sr = x_sum / len(centers)
y_sr = y_sum / len(centers)
print(x_sr,y_sr)