# str = "racecar"

def isPalin(str):
    # status = False
    # print(status)
    for i in range(len(str)-1):
        if str[i] != str[i-1]:
            return False
        else:
            return True
    
    # if status == True:
    #     print("Its a palindrome")
    # elif status == False:
    #     print("Its not a palindrome")


print(isPalin(str="racecar"))