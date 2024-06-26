#record store
countMe =0
x=0
#daily record
daily_record = (100,121,120,130,140,120,122,123,190,125)
#uder 120  == reduse
for i in daily_record:
    
    if i >=140:
        
        if i< daily_record[8]:
            print(i)
            x+=1
# print("In the past 10day,",countMe," had reduce sale privouse day")
