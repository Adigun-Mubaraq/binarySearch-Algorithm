def binary_search(haystack, needle, min = 0, max = -1):
    
    if max == -1:
        max = len(haystack) - 1

    mid_index = (max + min) // 2

    if haystack[mid_index] == needle:
        return mid_index
    elif min == max:
        return -1
    elif haystack[mid_index] > needle:
        return binary_search(haystack, needle, min, mid_index - 1)
    elif haystack[mid_index] < needle:
        return binary_search(haystack, needle, mid_index + 1, max)

numbers = [1, 3, 5, 6, 12, 18, 22, 23]
key = 12

result = binary_search(numbers, key)

if(result == -1):
    print("Element can not be found")
else:
    print("Your Search Index is " + str(result))
