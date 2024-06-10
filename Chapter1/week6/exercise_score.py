#enter 90 100 A
#enter 80 90 B
#enter 70 80 c
#enter 60 70 D
#enter below 60 F

user_score = float(input("Enter score"))

if user_score >=0 and user_score<101:
    if 90<=user_score <=100:
        print("Grade A")
    elif 80<=user_score <90:
        print("Grade B")   
    elif 70<=user_score <80:
        print("Grade C")        
    elif 60<=user_score <70:
        print("Grade D")       
    else:
        print("Grade F")    
