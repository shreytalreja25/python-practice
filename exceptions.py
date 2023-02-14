def div(a,b):
    return a/b

try:
    ans = div(40,0)

except ZeroDivisionError as e:
    print(e, " Cant divide by 0 ")
    print(e.__class__)

except Exception as e:
    print("Something Went Wrong..." ,e)
    print(e.__class__)

try:
    ans = div(40,"a")

except ZeroDivisionError as e:
    print(e, " Cant divide by 0 ")
    print(e.__class__)

except Exception as e:
    print("Something Went Wrong..." ,e)
    print(e.__class__)