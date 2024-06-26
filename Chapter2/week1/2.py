#rang function
list1 = [10,20,30,40,50]
list2 =[1,2,3,4]
#it accpet the list
list2.extend(list1)

print(list2)

#list2.extend(100)  wrong

list2.extend([100])  #right
print(list2)