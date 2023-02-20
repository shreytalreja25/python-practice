'''
Divide and conquer is a powerful algorithmic technique that solves a problem by breaking it down into smaller subproblems, solving each subproblem independently, and then combining the solutions to obtain the final solution. The main idea behind this technique is to recursively divide a problem into two or more smaller subproblems, solve them independently, and then combine the results.

Here is an example of how to implement a divide and conquer algorithm in Python using the merge sort algorithm as an example:
'''

# input_str = input()
# arr = input_str.split()

def merge_sort(arr):
    """
    Sort an array using the merge sort algorithm.
    """
    if len(arr) > 1:
        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted left and right halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# arr=[1,2,3,4,5,5,6,8,3,2,5,1,4]
# merge_sort(arr)
# print(arr)

arr_alt=[1,2,3,4,5,5,6,8,3,2,5,1,4]
sorted_arr = arr_alt.copy()
merge_sort(sorted_arr)
print(arr_alt,"==[AFTER-SORTING]==>",sorted_arr)
# print(arr_alt)