#cinema chair 5x5
user_input = int(input("Enter number:"))
col_count=0
for row in range(0,user_input):
    print(" ")
    for col in range(0, user_input):
        col_count+=1
        print(col_count, end=' ')      