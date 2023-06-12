import random
def bin_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = round((low + high)/2)
        item_guess = list[mid]
        if item_guess == item:
            return mid
        elif item_guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = bin_search(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")