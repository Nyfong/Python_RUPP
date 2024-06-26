import json
data ='''
{
    "a": "a",
    "b": "b",
    "c": "c"
}
'''
# variable uses triple quotes (''') to handle the multiline JSON string.
json_data = json.loads(data)

#coide to ceate son data as book.json file
with open('book.json', 'w') as f:
    json.dump(json_data, f, indent="\t")
    
    
#name #gender #score #wieght 
#socre 80-100 ex
#70-80 good
#<60 failed