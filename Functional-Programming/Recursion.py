'''
Recursion is a powerful technique in functional programming where a function calls itself in order to solve a problem. It allows us to express algorithms in a concise and elegant way by breaking down a complex problem into smaller subproblems that are easier to solve.
'''

'''
Advantages : 
NEAT CODE 
SUB PROBLEMS MAKE THE COMPLETE SOLUTION EASIER TO FIND
EASY TO DEBUG AND FIND ISSUES
'''


# EXAMPLE CODE OF RECURSION : 


input_str = input("Enter Array to be searched")
arr = input_str.split()
target = input("Enter element to be searched : ")
low  = input() 
high = input()


def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr,target,low,mid-1)
    else:
        return binary_search(arr,target,mid+1,high)
