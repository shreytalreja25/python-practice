# For loop : used for iterating a sequence in a known range.
# TO-DO : Understand how and when to use break & continue
str = 'Looping'

for item in str:
    print(item,end="")

arr = ["ABC","DEF","XYZ","GHI"]
for idx,item in enumerate(arr) :
    print(idx,item)


# While loop
count = 0
while count < len(arr):
    print(arr[count])
    count = count + 1

arr_alt = ["123","456","789"]
search = str(input("Enter an input : "))
for idx,item in enumerate(arr_alt):
    if item == search : 
        print("Search result found at " + str(idx+1))
        break
    else:
        print("Not found in arr_alt")
        
