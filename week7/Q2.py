#find the Cooefinate and determine which quadrant
user_x = int(input("Enter x num"))
user_y = int(input("Enter y num"))
if user_x and user_y == 0:
    print("Center of the Coordinate")
elif user_x>0 and user_y >0:
    print("1st quadrant")
elif user_x<0 and user_y >0:
    print("2nd quadrant")    
elif user_x<0 and user_y <0:
    print("3rd quadrant")    
elif user_x>0 and user_y <0:
    print("4th quadrant")    
    
        
        