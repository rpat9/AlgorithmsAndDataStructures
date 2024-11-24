import queue
 
class LinkedBinaryTree:
    
    class _Node:
        
        __slots__ = '_el', '_l', '_r'
 
        def __init__(self, element, left=None, right=None):
            self._el = element
            self._l = left
            self._r = right
 
 
    def __init__(self):
        self._root = None
        self._size = 0
 
 
    def __len__(self):
        return self._size
 
 
    def height(self):
        return self._height(self._root)
 
 
    def _height(self, p):
        
        if not p:
            return 0
        return 1 + max(self._height(p._l), self._height(p._r))
 
 
    def _in_order(self, p):
        
        if p:
            yield from self._in_order(p._l)
            yield p._el
            yield from self._in_order(p._r)
 
 
    def _pre_order(self, p):
        
        if p:
            yield p._el
            yield from self._pre_order(p._l)
            yield from self._pre_order(p._r)
 
 
    def _post_order(self, p):
        
        if p:
            yield from self._post_order(p._l)
            yield from self._post_order(p._r)
            yield p._el
 
 
    def breadth_first(self):
        
        q = queue.Queue()
        q.put(self._root)
        
        while not q.empty():
            
            p = q.get()
            
            if p:
                print(p._el)
                if p._l:
                    q.put(p._l)
                if p._r:
                    q.put(p._r)
 
 
    def bst_insert(self, key):
        
        if self._root is None:
            self._root = self._Node(key)
            
        else:
            self._bst_insert(self._root, key)
            
        self._size += 1
 
 
    def _bst_insert(self, node, key):
        
        if key < node._el: # Insert in the left subtree
            if node._l is None:
                node._l = self._Node(key)
            else:
                self._bst_insert(node._l, key)
                
        else: # Insert in the right subtree
            if node._r is None:
                node._r = self._Node(key)
            else:
                self._bst_insert(node._r, key)
 
 
    def bst_search(self, key):
        return self._bst_search(self._root, key)
 
 
    def _bst_search(self, node, key):
        
        if node is None:
            return False # If key is not found
        
        elif key == node._el:
            return True # If key is found
        
        elif key < node._el:
            return self._bst_search(node._l, key) # Search the left subtree
        
        else:
            return self._bst_search(node._r, key) # Search the right subtree
 
 
    def print_in_order(self):
        for key in self._in_order(self._root):
            print(key, end=' ')
        print() # adds a new line after traversal
 
if __name__ == "__main__":
    tree = LinkedBinaryTree()
    for value in [7, 3, 2, 5, 6, 9, 1, 4, 8, 10]:
        tree.bst_insert(value)
 
    print("Search for 4:", tree.bst_search(4)) # true
    print("Search for 12:", tree.bst_search(12)) # false
 
    print("In-order traversal:")
    tree.print_in_order()