# Create a function that takes 2 sorted arrays and merges them into one sorted array.
# For example, array1 = [1,3,5,7],
#              array2 = [4,4,6,8],
# The result should be array = [1,2,3,4,5,6,7,8]

def merge_sorted_arrays(arr1, arr2) -> list:
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    
    new_arr = []
    array1_item = arr1[0]
    array2_item = arr2[0]
    i = j = 1

    while (array1_item or array2_item):
        if array1_item < array2_item and array1_item!= False:
            new_arr.append(array1_item)
            if i < len(arr1):
                array1_item = arr1[i]
                i+=1
            else:
                array1_item = False
        else:
            new_arr.append(array2_item)
            if j < len(arr2):
                array2_item = arr2[j]
                j+=1
            else:
                array2_item = False

    return new_arr


print(merge_sorted_arrays([1,3,5,7], [2,4,6,8]))
print(merge_sorted_arrays([], [2,4,6,8]))
print(merge_sorted_arrays([1,3,5,7], []))
print(merge_sorted_arrays([], []))
print(merge_sorted_arrays([2,3,7,9], [0,1,3,8,11,14]))