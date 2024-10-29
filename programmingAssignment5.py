'''
Implement a function that takes in two sorted lists and merges them into one list, the new list must be sorted. 
The function MUST run in O(m+n), where m is the length of list 1 and n the length of list 2. 
In other words, the function cannot do more than one pass on list 1 and list 2.
'''

def merge_sorted_lists(list1, list2):
    
    """
    This function merges two sorted lists into one sorted list.
 
    Parameters:
    list1 (list): The first sorted list.
    list2 (list): The second sorted list.
 
    Returns:
    list: A sorted list that contains all elements from list1 and list2.
    """
    
    merged_list = []
    
    # Set up inital pointers
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        
        # Compare list1 and list2, add smaller element and increment pointer
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Add remaining elements if any from list 1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    # Add remaining elements if any from list 2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
 
    return merged_list
 
 
if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 6, 8, 10]
    print(merge_sorted_lists(list1, list2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list3 = [1, 3, 5, 7]
    list4 = [2, 4, 6, 8, 9, 10]
    print(merge_sorted_lists(list3, list4))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]