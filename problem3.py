#Write a Python program to implement a binary search algorithm for a sorted list of numbers.
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  

# list lai sort garcha ani binary search use garcha
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = int(input("Enter the number to search for: "))


index = binary_search(numbers, target)
if index != -1:
    print(f"Number found at index {index}.")
else:
    print("Number not found in the list.")
