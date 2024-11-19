def adul_func(n):
    if n>= 19:
        return True
    else:
        return False
ages = [19,29,34,29,18]
print('adult list:')
for a in filter(adul_func, ages):
    print(a, end=' ')
    