#Apple Grape Melon Orange 5000 6000 8000 2000
#Menu
print("======================")
print("1.Apple [5000 won]")
print("3.Grape [6000 won]")
print("3.Melon [8000 won]")
print("4.Orange [2000 won]")
print("======================")
list = ["Apple","Grape","Melon","Orange"]
listPrice = [ 5000 ,6000 ,8000, 2000 ]
user_pro = int(input("Enter the code you(1-4):"))
user_qty = int(input("Enter quantity of the product:"))
user_price = listPrice[user_pro - 1]
user_total = user_qty * user_price
print("Your buying:", list[user_pro])
user_cash = float (input("Enter Cash:"))
if user_cash > user_total:
    user_cash = user_cash - user_total
    print("Your cash back",user_cash)
    