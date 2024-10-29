class BinaryTree:
    
    class _Node:
        def __init__(self, e, left=None, right=None):
            self._left = left
            self._right = right
            self._element = e
 
 
    def __init__(self):
        self._root = None
        self._size = 0
 
 
    def is_empty(self):
        return self._root is None
 
 
    def add_root(self, e):
        if self._root:
            return None
        self._root = self._Node(e)
        return self._root
 
 
    def add_left(self, e, p):
        p._left = self._Node(e)
        return p._left
 
 
    def add_right(self, e, p):
        p._right = self._Node(e)
        return p._right
 
 
    def height(self):
        return self._height(self._root)
 
 
    def _height(self, v):
        if not v:
            return -1
        x = self._height(v._left)
        y = self._height(v._right)
        return 1 + max(x, y)


    def countK(self, k):
        return self._countK(self._root, k) 
 
 
    def _countK(self, p, k):
        if not p:
            return 0
        
        count = 1 if p._element == k else 0
        count += self._countK(p._left, k)
        count += self._countK(p._right, k)
        
        return count
 
 
    def equal(self, other):
        return self._equal(self._root, other._root)
       
 
    def _equal(self, p1, p2):
        if p1 is None and p2 is None:
            return True
        elif p1 is None or p2 is None:
            return False
        elif p1._element != p2._element:
            return False
        
        return self._equal(p1._left, p2._left) and self._equal(p1._right, p2._right)
 
 
if __name__ == '__main__':
 
    bt1 = BinaryTree()
    root1 = bt1.add_root(10)
 
    # Create a tree with height 5 and multiple 7's in it
    left_child1 = bt1.add_left(7, root1)
    right_child1 = bt1.add_right(7, root1)
 
    l1 = bt1.add_left(5, left_child1)
    r1 = bt1.add_right(7, left_child1)
 
    l2 = bt1.add_left(3, l1)
    r2 = bt1.add_right(6, l1)
 
    l3 = bt1.add_left(7, l2)
    r3 = bt1.add_right(4, l2)
 
    bt1.add_left(1, l3)
    bt1.add_right(7, l3)
 
    bt2 = BinaryTree()
    root2 = bt2.add_root(10)
 
    # Create another identical tree
    left_child2 = bt2.add_left(7, root2)
    right_child2 = bt2.add_right(7, root2)
 
    l1 = bt2.add_left(5, left_child2)
    r1 = bt2.add_right(7, left_child2)
 
    l2 = bt2.add_left(3, l1)
    r2 = bt2.add_right(6, l1)
 
    l3 = bt2.add_left(7, l2)
    r3 = bt2.add_right(4, l2)
 
    bt2.add_left(1, l3)
    bt2.add_right(7, l3)
 
    print("Height of bt1:", bt1.height())
    print("Count of 7 in bt1:", bt1.countK(7))
    print("Are bt1 and bt2 equal?", bt1.equal(bt2))
 
    # Making bt2 different from bt1
    bt2.add_left(100, l3)
    print("Are bt1 and bt2 equal after modification?", bt1.equal(bt2))