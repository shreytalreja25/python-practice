name = input("Enter your Name : ")
print("Hello " + name)

num1 = input("Enter Number 1 : ")
num2 = input("Enter Number 2 : ")

print(type(num1))
print(type(num2))

# To add two nos that are string types currently we now need to convert them into integers
sum = str(int(num1) + int(num2)) 

print(type(num1))
print(type(num2))

print("Sum of Num1 and Num2 : " + sum )

# Working with strings...

first = input("Enter first name : ")
last = input("Enter last name : ")
print("Hello {} {}".format(first,last))