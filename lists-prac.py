# Lists are mutable collection of indexed objects that can contain a variety of data types

# Ways to declare a list

list1 = [1,2,3,4,5]
list2 = ["A","B","C","D","E"]
list3 = [True,"Hello World",1,"A"]
list4 = ["A",[1,2,3],True,10.5] #Lists can also contain a list as an object

# Ways to print a list

print(*list1)

print(list2,sep=" ")

for i in list3:
    print(i)

# Insert data into a list using the insert() function
# listname.insert(at_which_index,what-value-to-insert)

list1.insert(len(list1),6)
print(*list1)

# Using append function to append a item to the end

list2.append("F")
print(*list2)

# Using extend function to add a bunch of values at the end

list1.extend([7,8,9,10])
print(*list1)

# Using pop function to remove a value
# list_name.pop(index)

list1.pop(4)
print(*list1)

# Using del keyword to delete a value from a list

del list1[2]
print(*list1)

# We can iterate over a list

for x in list4:
    print(x,end=" ")


# for i in list1:
#     list2 = []
#     print(i)
#     list1[i] = list2.push()
#     del list1[i]