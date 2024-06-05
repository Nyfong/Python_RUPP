#while loop with the sum of postive number
user_input = int (input('Enter the number to make it sum'))
i=0
sum =0
while user_input > 0 and i < user_input:
    i+=1
    sum+=i
print(sum)    
