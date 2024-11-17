from maps.unsorted_table_map import UnsortedTableMap


class UnsortedMapOfLists(UnsortedTableMap):

    def __getitem__(self, position: tuple):
        # When position is 1 we return the entire array assuming that only the key is given
        if len(position) == 1:
            return super().__getitem__(position)

        key, index = position

        head: list = super().__getitem__(key)

        if index >= len(head):
            raise IndexError("Size of array associated with key: ", key, " is: ", len(head))
        return head[index]


    def __setitem__(self, position: tuple, value):

        if len(position) == 1:
            super().__setitem__(position, value)
            return

        key, index = position
        try:

            head: list = super().__getitem__(key)
            if index < len(head):
                # overrite exiting value, or append
                head[index] = value
            elif index == len(head):
                head.append(value)
            else:
                raise IndexError("Size of array associated with key: ", key, " is: ", len(head))

        except KeyError:
            # new key, create a list for the key
            head = [value]
            self._table.append(self._Item(key, head))


    def __delitem__(self, position: tuple):
        
        # When position is 1 we remove the entire array associated with the key
        if len(position) == 1:
            
            key = position[0]
            super().__delitem__(key)
            
        else:
            
            key, index = position
            head: list = super().__getitem__(key)
            
            if index >= len(head):
                raise IndexError("Size of array associated with key: ", key, " is: ", len(head))
            
            del head[index] # Removes element at the specified index
            
            if not head:
                super().__delitem__(key) # Remove the key if array will be empty after deleting
        
        raise Exception("Implement me")
    

def swap_arrays(mapA, key1, key2):
    array1 = mapA[key1]
    array2 = mapA[key2]
    mapA[key1] = array2
    mapA[key2] = array1



if __name__ == "__main__":
    
    m = UnsortedMapOfLists()
    m["a", 0] = 5
    m['a', 0] = 50
    m['a', 1] = 60
    m['b', 0] = 2
    m['c', 1] = 10
    m['d'] = [10, 20, 30]
    
    # Print all initial values
    print("Before Map:")
    print("m['a', 0]:", m['a', 0])
    print("m['a', 1]:", m['a', 1])
    print("m['b', 0]:", m['b', 0])
    print("m['a']:", m['a'])
    print("m['d']:", m['d'])

    # Test deletion method
    print("\nAfter deleting m['b', 0]:")
    
    del m['b', 0]
    
    try:
        print(m['b'])
    except KeyError:
        print("Key 'b' not found.")



    print("\nAfter deleting m['c']:")
    
    del m['c']
    
    try:
        print(m['c'])
    except KeyError:
        print("Key 'c' not found.")
        
    # Testing swapping arrays
    swap_arrays(m, 'a', 'd')

    print("\nAfter swapping 'a' and 'd':")
    print("m['a']:", m['a'])
    print("m['d']:", m['d'])