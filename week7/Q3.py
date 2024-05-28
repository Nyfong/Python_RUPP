#user menu
#b buger , c chicken , p pizza
list_food = ["burger", "chicken", "pizza"]
list_order =["b","c","p"]
print("B burger")
print("C chicken")
print("P pizza")
user_input = input("Enter a menu (b,c,p)")
if user_input== list_order[0]:
    print("you chooese",list_food[0])
elif user_input== list_order[1]:
    print("you chooese",list_food[1])    
elif user_input== list_order[2]:
    print("you chooese",list_food[2])    
else:
    print("NONE")    
