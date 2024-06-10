#print stages from 1 to 9
n = 1
i =1
sum =0

while n <10 :
    
    while i<11:
        sum = n*i
        i+=1
        print(n,"x",i-1,"=",sum)
    n+=1
    i=1
    print(n)