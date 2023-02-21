# List comprehension
# SYNTAX : [<expression> for x in <sequence> if <condition>]

data = [2,3,4,6,7,8,9]

# Ex1 : List comprehension : updating the same list
data = [x+3 for x in data]
print("Updating the list",data)

# Ex2 : List comprehension: creating a different list with updated values
new_data = [x+2 for x in data]
print("Creating new list : ", new_data)

# Ex3 : With an if-else condition : Multiples of four
fourx = [x for x in new_data if x%4==0]
print("Multiples of four : ",fourx)

# Ex4 : Divisible by four minus one 
fourminusone = [x-1 for x in new_data if x%4==0]
print("Divisible by four minus one", fourminusone)

# Using range function 
nines = [x for x in range(1,100) if x%9 == 0]
print("Nines : ",nines)

# Dictionary comprehension
# dict = {key:value for key,value in <sequence> in <condition> }

# Using range function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range () ", usingrange)

# Lists
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create a dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key,value) in zip(number,months)}
print("Using two lists : ",months_dict)

# Set comprehension







# Generator comprehension