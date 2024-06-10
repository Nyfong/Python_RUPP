#simulation for goalkeeper
import random
goalkeeper = random.randint(1,3)
user_shot = (input("Kick from (left right middle)"))

position =""
#condition
if (goalkeeper == 1):
    position ="left"
elif (goalkeeper ==2):
    position ="right"    
elif (goalkeeper == 3):
    position ="middle"      
elif(user_shot != position):
    print("Congrat!! you input",user_shot,"And GoalKeeper:",goalkeeper,position)
else:
    print("You lose:",user_shot,"And GoalKeeper:",goalkeeper,position)