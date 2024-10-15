with open('files\\27_A.txt') as f:
    lines = f.readlines()
coords = []
matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
for line in lines:
    zxc = line.split()
    zxc = [float(i) for i in zxc]
    coords.append(zxc)
for i in coords:
    if i[0] >= 0 and i[0] <= 1 and i[1] >= 0 and i[1] <= 1:
       matrix[2][0] = matrix[2][0] +1 
    if i[0] >= 1 and i[0] <= 2 and i[1] >= 0 and i[1] <= 1:
       matrix[2][1] = matrix[2][1] + 1    
    if i[0] >= 2 and i[0] <= 3 and i[1] >= 0 and i[1] <= 1:
       matrix[2][2] = matrix[2][2] + 1
       
    if i[0] >= 0 and i[0] <= 1 and i[1] >= 1 and i[1] <= 2:
       matrix[1][0] = matrix[1][0] + 1
    if i[0] >= 1 and i[0] <= 2 and i[1] >= 1 and i[1] <= 2:
       matrix[1][1] = matrix[1][1]  + 1    
    if i[0] >= 2 and i[0] <= 3 and i[1] >= 1 and i[1] <= 2:
       matrix[1][2] = matrix[1][2] + 1 
    
    if i[0] >= 0 and i[0] <= 1 and i[1] >= 2 and i[1] <= 3:
       matrix[0][0] = matrix[0][0] + 1
    if i[0] >= 1 and i[0] <= 2 and i[1] >= 2 and i[1] <= 3:
       matrix[0][1] = matrix[0][1] + 1    
    if i[0] >= 2 and i[0] <= 3 and i[1] >= 2 and i[1] <= 3:
       matrix[0][2] = matrix[0][2] + 1 
print(matrix[0],matrix[1],matrix[2],sep='\n')