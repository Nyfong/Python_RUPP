from collections import defaultdict
tup = ('A','B','C')
z = dict.fromkeys(tup)
z = defaultdict(int)
print(z['A'])