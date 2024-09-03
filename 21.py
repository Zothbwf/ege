with open("E:\\downloads\\24_21.txt") as file:
    string = file.read()
count = 0 
count_list = []
for i in range(1,len(string)):
    if string[i-1] == string[i]:
        count_list.append(count)
        count = 0
    count = count + 1
print(max(count_list))