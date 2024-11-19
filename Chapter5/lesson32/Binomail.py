def fibo(n,k):
    if k == 0 or n == k:
        return 1
    else:
        return fibo(n-1, k-1) + fibo(n-1, k)
print(fibo(1,0))