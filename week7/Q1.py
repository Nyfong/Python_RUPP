#user input for calculate using codintion with operation
user_option = int(input("Enter number [1]+ [2]- [3]* [4]/"))
user_num1= int(input("Enter Num1: "))
user_num2= int(input("Enter Num2: "))
user_result =0
if user_option == 1 and user_option >0:
     #addition
     user_result = user_num1 + user_num2
     
elif user_option == 2 and user_option >0:
    #substract
    user_result = user_num1 - user_num2
elif user_option == 3 and user_option >0:         
    user_result = user_num1 * user_num2
elif user_option == 4 and user_option >0:             
    user_result = user_num1 / user_num2
elif user_result<0 and user_result>4:
    print("Could not find")    
    
print("The result = ", user_result)            
    
