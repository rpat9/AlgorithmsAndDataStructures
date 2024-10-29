class Empty(Exception):
    pass

class Stack:
    # Straight forward use of adapter patter, re-use Python List
    def __init__(self):
        self._data = [] # list as underlying storage

    def is_empty(self):
        """is stack empty"""
        return len(self._data) == 0

    def len(self):
        return len(self._data)

    def top(self):
        if self.is_empty():
            raise Empty()

        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty()

        return self._data.pop()

    def push(self, element):
        self._data.append(element)