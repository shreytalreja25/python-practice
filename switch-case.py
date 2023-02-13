# Using switch case statement as an alternative to if/else/elif

http_status = 200

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Page not found")
    case 500 | 501:
        print("Unknown")