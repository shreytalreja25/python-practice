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
