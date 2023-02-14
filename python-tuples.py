# In Python, a tuple is an ordered collection of elements, which can be of different data types such as integers, strings, or other objects. Tuples are similar to lists, but they are immutable, which means that once a tuple is created, its elements cannot be modified. Tuples are defined using parentheses () and separated by commas, like this: (1, "hello", 3.14). They are often used to represent data that should not be changed, such as coordinates or settings for a program.

my_tuple = (1,1,2,1,1,2,2,'strings',3.14,True)

# How to count occurences of a value in a tuple

print(my_tuple.count(2))

# Find the index of a value of a value in a tuple

print(my_tuple.index(1))

# Immutability

# my_tuple[3] = "New Value"
# This will return an error