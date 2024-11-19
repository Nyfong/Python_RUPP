#a tuple call study_tup
from collections  import defaultdict
study_tup = (
    ('211101','Devide Doe', '010-20-209-29'),
    ('211102','John Smith', '010-20-209-29'),
    ('211103','Jane Carter', '010-20-209-29'),
)
tupList = dict.fromkeys(study_tup)
#
list = []
list_2 =[]
list_2D = []
#for data
for i in range(3):
    for j in range(2):
        list_2D.append(study_tup[i][j])

list_2  = list_2D[:2]
list_3 = list_2D[2:4]
list_4 = list_2D[4:6]
listFull =[]
listFull.append(list_2)
listFull.append(list_3)
listFull.append(list_4)
#print(listFull)     

#for id
for i in range(3):
    for j in range(1):
        list.append(study_tup[i][j])
#add key

#print(list)        
for i in range(2):
    key = dict.fromkeys(list, listFull[i])
print(key)

