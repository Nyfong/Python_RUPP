

S = [11, 37, 45, 26, 59, 28, 17, 53]
x = 11

def seq_search (list,param):
    for i in range(len(list)):
        if param == list[i]:
            return i
    return -1    
pos = seq_search(S,x)
print("sequence function:",pos)

