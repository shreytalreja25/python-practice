# Algorithm for checking if a string is a palindrome or not 

# str = input("Enter a string to be checked : ")

def isPalin(str):
    
    startIndex = 0
    endIndex = len(str) - 1
    
    # str = input("Enter a string to be checked : ")
    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True

print(isPalin("malayalam"))
