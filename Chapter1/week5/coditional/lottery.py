n1,n2,n3 = 2,3,9
n=0
a, b, c = input("Enter three degit:").split()
a= int(a)
b= int(b)
c= int(c)
if a == n1 or a == n2 or a == n3 :
    n+=1
if b == n1 or b ==n2 or b== n3 :
    n+=1
if c ==n3 or c==n1 or c == n2:
    n+=1
if n==3:
    print("You won",n," points")    
else:
    print("You lost")
