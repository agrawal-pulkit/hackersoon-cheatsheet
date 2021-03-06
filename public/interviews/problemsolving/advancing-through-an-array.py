"""
Advancing through an array.
"""

def iterateArray(arr):
    furthest_reach_so_far, last_index = 0, len(arr) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far <= last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, arr[i] + i)
        print(furthest_reach_so_far)
        i += 1
    return furthest_reach_so_far >= last_index 

arr = [3,3,1,0,2,0,1]
print(iterateArray(arr))