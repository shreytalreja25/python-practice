# Using match case statement as an alternative to if/else/elif
# Match statements takes a variable and compares its values to several different conditions until one is met 

http_status = int(input("Enter HTTP Status : "))

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Page not found")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Undefined request")
