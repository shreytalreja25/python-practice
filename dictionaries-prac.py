# In Python, a dictionary is an unordered collection of key-value pairs, where each key is unique and maps to a corresponding value. Dictionaries are also sometimes referred to as "maps" or "associative arrays" in other programming languages.

# Dictionaries are defined using curly braces {} and each key-value pair is separated by a colon. For example, {"apple": 1, "banana": 2, "orange": 3} is a dictionary with three keys and their corresponding values.

# You can access the value of a specific key in a dictionary using the key in square brackets, like this: my_dict["apple"]. You can also modify the value of an existing key or add a new key-value pair using the same syntax. Dictionaries are commonly used to store and retrieve data that can be looked up by a unique identifier or key.

my_dict = {0:'Water',1:'Coffee',2:'Tea',3:'Milk',"Name":"Shrey"}
print(my_dict["Name"])

# Modify values of a key
my_dict[2] = "Earl Grey Tea"
print(my_dict[2])

# Delete values of a key
del my_dict[3]

# Iterate over a dictionary

for key,value in my_dict.items():
    print(str(key) + " : " + str(value))
