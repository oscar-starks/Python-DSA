def binary_search(array, lower, higher , num):
    if num in array:
        index = (higher+lower)//2
        if array[index] == num:
            return index
        elif array[index] > num:
            return binary_search(array, lower, index-1, num)
        elif array[index] < num:
            return binary_search(array,index + 1, higher, num)
    else:
        return "Number does not exist in the array"
        
print(binary_search(sorted([1,3,4,5,6,7,8,9,10]), 0, len([1,3,4,5,6,7,8,9,10])-1, 5 ))