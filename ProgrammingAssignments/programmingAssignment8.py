'''
Implement a singly linked list with following functions:
- add_head(e)
- add_tail(e)
- find_3rd_to_last() - returns element located at third-to-last in the list
- reverse() - reverse the linked list, note, this is not just printing elements in reverse order, this is actually reversing the list
'''

class Node:
    """
    This class represents a node in a singly linked list.
    Each node has a value and a reference to the next node in the list.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None
 
class SinglyLinkedList:
 
    def __init__(self):
        self.head = None
        self.tail = None
 
    def add_head(self, e):
        newNode = Node(data=e)             # Create a new node
        newNode.next = self.head           # Set next to current head
        self.head = newNode                # Update head to point to new node
        return None
        
 
    def add_tail(self, e):
        newNode = Node(data=e)
        
        if self.head is None:              # Whether or not the list is empty, if so update head to newNode
            self.head = newNode
        else:
            current = self.head            # Setting up to traverse to the last node
            while current.next:            # Traversing to the last node
                current = current.next
            current.next = newNode         # Update the last node once reached
        return None    
 
 
    def find_3rd_to_last(self):
        pointerOne = self.head
        pointerTwo = self.head
        
        for _ in range(3):
            if pointerOne is None:         # Returns None if list is smaller than 3
                return None
            pointerOne = pointerOne.next   # Moves pointer1 three spaces ahead
            
        while pointerOne:                  # Move both pointers until first reaches end
            pointerOne = pointerOne.next
            pointerTwo = pointerTwo.next
        
        return pointerTwo.data if pointerTwo else None 
 
 
    def reverse(self):
        current = self.head
        previous = None
        
        while current:
            next_node = current.next       # Store the next node
            current.next = previous        # Reverse the current node's pointer
            
            previous = current             # Move the previous pointer forward
            current = next_node            # Move to the next node
        
        self.head = previous               # Update the head to the new front
        
        return None
    
 
if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    linked_list.add_head(1)
    linked_list.add_tail(2)
    linked_list.add_tail(3)
    linked_list.add_tail(4)
    print(linked_list.find_3rd_to_last())  # 2
    linked_list.reverse()
    print(linked_list.find_3rd_to_last())  # 3