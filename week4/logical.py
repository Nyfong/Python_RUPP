#find the  odd number
odd = int (input("Enter an integer number:"))
print( "Is this an odd number?" ,odd%2 != 0)


even_number = int (input("Enter an integer number"))
if 0< even_number< 100 and even_number %2 == 0:
    print("It's an even number and it's between 0 to 100", even_number %2 == 0)
else:
    print("I dont know")    