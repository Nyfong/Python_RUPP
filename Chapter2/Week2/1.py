import json
data =[
     {
    "coffe":
        {
            "ice":{
                "ice amaricano":100,
                "ice latte":200
            },"hot":{
                "ice amaricano":100,
                "ice latte":200
            }
        },
    "food":
        {
            "ice":{
                "ice amaricano":100,
                "ice latte":200
            },"hot":{
                "ice amaricano":100,
                "ice latte":200
            }
        }         
    },
     {
    "coffe":
        {
            "ice":{
                "ice amaricano":100,
                "ice latte":200
            },"hot":{
                "ice amaricano":100,
                "ice latte":200
            }
        },
    "food":
        {
            "ice":{
                "ice amaricano":100,
                "ice latte":200
            },"hot":{
                "ice amaricano":100,
                "ice latte":200
            }
        }         
    }
]
json_data = json.dumps(data)
print("Parsed JSON data:", json_data)