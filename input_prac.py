def location_input():
    print("Where do you live ?")
    location = input()
    print("So you live in : " + location)
    print("Is this correct ? Enter Y/N to continue...")
    check = input()
    return check

def location_intake():
    check = location_input()
    if(check == 'Y'):
        # Enter query for passing data into db
        print("Data Saved successfully")
    
    elif(check == 'N'):
        print("Data not saved. Enter location again : ")
        location = input()
        location_input(location)

    else:
        print("Please check your input")
        location_input()

location_input()
location_intake()