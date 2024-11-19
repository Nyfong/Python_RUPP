print("Start Cafe menu program..........Press q to quit:")
cafe_menu = {"ice cafes": 3000} #dicstionary
while True:
    str = input("$")
    if str.startswith('q'):
        break;
    command = str[0]
    
    if command == '<':
        str = str.replace("<", "")
        inputStr = str.split(':')
        if len(inputStr)<2:
            print("error")
            continue
        else :
            cafe_menu[inputStr[0].strip()] = inputStr[1].strip()
        
    elif command ==">":
        str = str.replace(">", "")
        inputStr = str.strip()
        if inputStr in cafe_menu:
            print(cafe_menu[inputStr])
        
        else:
            print('{} not in the menu'.format(inputStr))
    
    elif command =='q':
        break
    else:
        print('input error')

print('exting the menu')        
        
        