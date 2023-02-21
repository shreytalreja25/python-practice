'''
A pure function is a function that always produces the same output for a given input and does not modify any data outside of its scope. In other words, it has no side effects and is entirely deterministic. Pure functions are useful because they make code easier to reason about, test, and debug. Here is an example of a pure function in Python:
'''

def add_numbers(x, y):
    return x + y
# This is a pure function

my_list = [1,2,3]

def add_to_list(lst,item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_to_list(my_list,4)
print(my_list,"++Adding a new item at end++",new_list)
# print(new_list)  
