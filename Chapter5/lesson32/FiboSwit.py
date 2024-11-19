
def fib3(F, n):
    if n <= 1:
        return F[n]
    else:
        if F[n] < 0:
          F[n] = fib3(F, n - 1) + fib3(F, n - 2)
        return F[n]
N = int(input("Input A Number:"))
F= [0,1] + [-1] * (N-1)
print(fib3(F, N));