'''
*args: This syntax allows you to pass a variable number of positional arguments to a function. The *args syntax is used to capture all the non-keyword arguments in a function call and store them in a tuple. The * before args unpacks the arguments, allowing them to be passed into the function as separate arguments.
'''
def print_args(*args):
    for arg in args:
        print(arg)
        # print(type(arg[4]))

print_args(1,2,3,4,"String type",[12,34,35])
# I can pass any variable number of arguments inside this function and it will accept it and can be accessed using a for loop

'''
**kwargs: This syntax allows you to pass a variable number of keyword arguments to a function. The **kwargs syntax is used to capture all the keyword arguments in a function call and store them in a dictionary. The ** before kwargs unpacks the keyword arguments, allowing them to be passed into the function as separate keyword arguments.
'''