'''

In Python, a list is a collection of items that can be of any data type. Lists are a commonly used data structure because they allow you to store and manipulate multiple values in one place. You can add, remove, or modify elements of a list, and you can perform many operations on the entire list, such as sorting, reversing, or searching for specific elements.

List comprehension is a shorthand way to create a new list from an existing list or other iterable. It is a compact and elegant way to write code that performs some operation on each element of a list and returns a new list as the result. List comprehension is a Pythonic way of writing code, and it can make your code more concise, readable, and efficient.

Here are the steps to use list comprehension:

    Start with an existing list or other iterable.
    Write an expression that performs some operation on each element of the list, and returns the result as a new element in the new list. This expression can be a simple arithmetic operation, a function call, a conditional expression, or a combination of these.
    Enclose the expression in square brackets, and place it inside a pair of parentheses.
    Add any necessary conditions or filters to the expression using the if keyword.
    Assign the resulting list to a variable, or use it directly in your code.

Here is an example of list comprehension that creates a new list of even numbers from an existing list:

'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers) # Output: [2, 4, 6, 8, 10]

odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers) # Output: [1, 3, 5, 7, 9]

'''
In this example, the original list numbers is used to create a new list even_numbers that contains only the even numbers. The expression inside the square brackets is x, which is the value of each element in numbers. The condition if x % 2 == 0 filters out all the odd numbers, and returns only the even numbers. Finally, the resulting list is assigned to the variable even_numbers.
'''