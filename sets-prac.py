# In Python, a set is an unordered collection of unique elements. Sets are similar to lists and tuples, but unlike lists and tuples, they do not have a defined order, and each element can only appear once. Sets are defined using curly braces {} or the set() function, and individual elements are separated by commas. For example, {1, 2, 3} or set([1, 2, 3]) creates a set of three integers. Sets are useful when you need to perform mathematical operations such as union, intersection, and difference on collections of elements.

set_a = {1,2,3,4,5,5,6,6,6,7}

print(set_a) # Set eliminates multiple copies of the same value

# To add a new value to the set

set_a.add(8)
print(set_a)

# Remove a value from a set

set_a.remove(6)
print(set_a)