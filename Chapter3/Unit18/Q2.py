def thepow(n, x):
    if x == 0:
        return 1
    else:
        return n*thepow(n,x-1)
print(thepow(2,10))