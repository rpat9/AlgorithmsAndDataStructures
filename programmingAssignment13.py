def merge_and_count(arr, left, mid, right):
    
    # 1. Initialize inversion count to 0.
    inv_count = 0
    
    # 2. Create temporary arrays to hold the values of the left and right halves of the original array.
    left_temp = arr[left:mid+1]
    right_temp = arr[mid+1:right+1]
    
    # 3. Initialize counters and indices for merging.
    i = 0
    j = 0
    k = left
    
    # 4. Merge the two halves and count inversions.
    while i < len(left_temp) and j < len(right_temp):
        if left_temp[i] <= right_temp[j]:
            arr[k] = left_temp[i]
            i += 1
        else:
            arr[k] = right_temp[j]
            j += 1
            inv_count += len(left_temp) - i
        k += 1
   
    # 5. Copy any remaining elements from the left and right temporary arrays back to the original array.
    while i < len(left_temp):
        arr[k] = left_temp[i]
        i += 1
        k += 1
    
    while j < len(right_temp):
        arr[k] = right_temp[j]
        j += 1
        k += 1
    
    # 6. Return the inversion count.
    return inv_count
 
 
def merge_sort_and_count(arr, left, right):
    # 1. Initialize inversion count to 0.
    inv_count = 0
    
    # 2. If the left index is less than the right index:
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_and_count(arr, left, mid)
        inv_count += merge_sort_and_count(arr, mid + 1, right)
        inv_count += merge_and_count(arr, left, mid, right)
    
    # 3. Return the total inversion count.
    return inv_count
 

def count_inversions(input_list):
    # 1. Create a copy of the input list to avoid modifying the original list.
    arr = input_list.copy()
    
    # 2. Call merge_sort_and_count with the copied array, starting indices 0 and ending index (length of array - 1).
    
    # 3. Return the total inversion count.
    return merge_sort_and_count(arr, 0, len(arr) - 1)

 
# Example usage:
if __name__ == "__main__":    
    input_list = [5,4,3,2,1]
    print(count_inversions(input_list))  # Output: 10
 
    input_list = [1,5,2, 8,3,4]
    print(count_inversions(input_list))  # Output: 5
 
    input_list = [1,2,3,4,5]
    print(count_inversions(input_list))  # Output: 0
    
    input_list = [1,2,3,5,4]
    print(count_inversions(input_list))  # Output: 1