
"""
Delete Duplicate from a sorted array.
And return number of duplicate entries after deletion.
"""
def delete_duplicate(arr):
    if len(arr) == 0:
        return
    
    write_index = 1
    for i in range(len(arr)): 
        if arr[write_index-1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1
    return arr[:write_index]

    

arr = [2,3,5,5,7,11,11,11,13]
result = delete_duplicate(arr)
print("result: ", result)