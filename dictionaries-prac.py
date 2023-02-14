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


# There are many methods available for dictionaries in Python. Some of the most commonly used methods include:

    # clear(): Removes all key-value pairs from the dictionary.
    # copy(): Returns a shallow copy of the dictionary.
    # get(key[, default]): Returns the value for a given key, or a default value if the key is not in the dictionary.
    # items(): Returns a view of the dictionary's key-value pairs as a list of tuples.
    # keys(): Returns a view of the dictionary's keys as a list.
    # pop(key[, default]): Removes and returns the value for a given key, or a default value if the key is not in the dictionary.
    # popitem(): Removes and returns an arbitrary key-value pair from the dictionary.
    # setdefault(key[, default]): Returns the value for a given key, or sets a default value if the key is not in the dictionary.
    # update([other]): Updates the dictionary with key-value pairs from another dictionary or iterable of key-value pairs.
    # values(): Returns a view of the dictionary's values as a list.