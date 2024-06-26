#introduction to the key and value
menu = {
    "a":1,
    "b":2,
    "c":3,
}
for key in menu:
    print("{:16s}price{:,}kw".format(key,menu[key]))
    