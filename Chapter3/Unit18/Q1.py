#calculate the factorail

def fac(n):
    if n<=1:
        return 1
    else:
        return fac(n-1)+n

print("The factorail:",fac(10))
    
        