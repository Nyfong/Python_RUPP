#assignment list to another list
list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9], 
]
list1 = list   #assginment list
print(list1)

list1[1][-2] = 1000;
print("Old", list)
print("New", list1)

