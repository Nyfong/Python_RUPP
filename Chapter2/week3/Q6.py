fruits_dic = {
    "apple": 6000,
    "melon": 3000,
    "banana":5000,
    "orange":4000 
}
melon ='melon'
apple = 'apple'
line =[]
for key in fruits_dic:
    line.append(key)
    if apple in key:
        print(apple,"is in key")
    if melon in key:
        print(melon,"is in key")
print(line)