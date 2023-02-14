# In Python, a set is an unordered collection of unique elements. Sets are similar to lists and tuples, but unlike lists and tuples, they do not have a defined order, and each element can only appear once. Sets are defined using curly braces {} or the set() function, and individual elements are separated by commas. For example, {1, 2, 3} or set([1, 2, 3]) creates a set of three integers. Sets are useful when you need to perform mathematical operations such as union, intersection, and difference on collections of elements.

set_a = {1,2,3,4,5,5,6,6,6,7}
set_b = {4,4,4,3,5,6,7,7,8,9,10}

print(set_a) # Set eliminates multiple copies of the same value

# To add a new value to the set
set_a.add(8)
print(set_a)

# Remove a value from a set
set_a.remove(6)
print(set_a)

set_a.remove(7)
print(set_a)

# For union of two sets
print("UNION OF SET A & B : ", set_a.union(set_b))
print("UNION OF SET A & B : ", set_a | set_b)

# Intersection of two sets
print("INTERSECTION OF SET A & B : ", set_a.intersection(set_b))
print("INTERSECTION OF SET A & B : ", set_a & set_b)

# Difference of two sets
print("DIFFERENCE OF SET A and B : ", set_a.difference(set_b))
print("DIFFERENCE OF SET A and B" , set_a - set_b)

# Symmetric difference of two sets
print("SYMMETRIC DIFFERENCE OF 2 SETS : ", set_a.symmetric_difference(set_b))
print("SYMMETRIC DIFFERENCE OF 2 SETS : ", set_a ^ set_b)

# Set objects are not ordered and hence cannot be indexed
# print(set_a[0]) -> Will return an error

