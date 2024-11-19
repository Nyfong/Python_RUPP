product_dec = {
    'Coffe':7,
    'Pen':3,
    'Paper cup':2,
    'Milk':1,
    'Coke':4,
    'Book':5,
    'call':[
        {
            "mom":[
                99669914,
                12231413,
            ]
        }
    ]
    
}
user_entered = input("Enter name of the item :")
for enter in product_dec:
    if user_entered == enter:
        print(product_dec[enter])
        break
      
        