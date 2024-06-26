list_simple = list(range(2, 11))
print("List of numbers from 2 to 10:", list_simple)
a =[11]
temp =[]
for n in list_simple:
    is_prime = True
    if n > 2:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
    if is_prime:
        temp.extend([n])
        
print(temp)

temp.extend(a)
print(temp)