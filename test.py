
# str = ["shrey"]
# str[0]
# print(str)

new_list = [1,2,3,4]
new_list.insert(0,0)
new_list.append(new_list)
new_list.append(5)
print(new_list[4])
print(new_list)


# Local Scope demo
def local_Scope():
    x = 15
    print(x)

local_Scope()
# print(x) --> Cannot access x [a local variable] from outside the function

# Enclosing scope demo
def Enclosing_Scope():
    x = 10
    print(x)
    def Inner_Func():
        y = 5
        print(y)
        print("Accessed from inner function : ",x)
    Inner_Func()
Enclosing_Scope()
# Enclosing scope : A function declared inside the function can access a variable declared in the outside function.

# Global Scope
x = 15
def Global_Scope():
    global x
    x = x + 10
    print(x)

Global_Scope()
print(x)

'''
In Python, the global keyword is used to indicate that a variable is in the global scope, i.e., it should be accessed and modified as a global variable, rather than as a local variable within a function.

When you use the global keyword inside a function to declare a variable, Python knows that you want to use the variable from the global scope, rather than create a new local variable with the same name. This means that any changes you make to the variable within the function will affect the global variable with the same name.
'''

# BuiltIn Scope demo
import math

def Builtin_Scope():
    x = 25
    print(int(math.sqrt(x)))

Builtin_Scope()

'''
Python has a built-in scope that contains all the built-in functions and modules, such as print(), len(), and math. These variables are available anywhere in the program without having to import anything.
'''


