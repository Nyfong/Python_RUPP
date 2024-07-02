list = []
num =0
for i in range(4):
    line =[]
    for j in range(4):
        num+=1
        line.append(num)    
    list.append(line)    
for i,j,k,h in list:
    print(i,j,k,h)
    
        