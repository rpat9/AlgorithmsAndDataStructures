import random
import enum
from abc import ABC, abstractmethod

'''
HeapPriorityQueue, UnsortedPriorityQueue, and SortedPriorityQueue classes are not provided in this folder
'''

from .PriorityQueues.heap_priority_queue import HeapPriorityQueue
from .PriorityQueues.unsorted_priority_queue import UnsortedPriorityQueue
from .PriorityQueues.sorted_priority_queue import SortedPriorityQueue


'Enum class, similiar to enums in Java, C, C++,...'
class SortingALgorithm(enum.Enum):
    PR_Queue = 1
    SortedPriorityQueue = 2
    UnSortedPriorityQueue =3

'Abstract class'
class Sorter(ABC):

    @abstractmethod
    def sort(self) -> list:
        """in strategy pattern naming, this is method execute"""
        pass


class PR_queue_sorter(Sorter):
    """ Heap sort Sorting according to the algorithm on slide #10 using a heap implementation
    of priority queue"""

    def __init__(self):
        self._q = HeapPriorityQueue()

    def sort(self, seq:list):
        while len(seq) > 0:
            self._q.add(seq[0], None)
            del seq[0]
        while not self._q.is_empty():
            k,v =self._q.remove_min()
            seq.append(k)
        return seq


class UnsortedPriorityQueueSorter(Sorter):
    def __init__(self):
        self._q = UnsortedPriorityQueue()
        
    def sort(self, seq: list) -> list:
        
        for e in seq:
            self._q.add(e, None)
            
        sortedSeq = []
        
        while not self._q.is_empty():
            minKey, v = self._q.remove_min()
            sortedSeq.append(minKey)
    
        return sortedSeq


class SortedPriorityQueueSorter(Sorter):
    
    def __init__(self):
        self._q = SortedPriorityQueue()
        
    def sort(self, seq: list) -> list:
        
        for e in seq:
            self._q.add(e, None)
        
        sortedSeq = []
        
        while not self._q.is_empty():
            minKey, v = self._q.remove_min()
            sortedSeq.append(minKey)
        
        return sortedSeq
        


class Context:
    def __init__(self, sorting_algo:SortingALgorithm):
        
        if sorting_algo == SortingALgorithm.PR_Queue:
            self._sorter = PR_queue_sorter()
        elif sorting_algo == SortingALgorithm.UnSortedPriorityQueue:
            self._sorter = UnsortedPriorityQueueSorter()
        elif sorting_algo == SortingALgorithm.SortedPriorityQueue:
            self._sorter == SortedPriorityQueueSorter()


    def strategy(self):
        """    The Context maintains a reference to one of the Strategy objects. The
               Context does not know the concrete class of a strategy. It should work
               with all strategies via the Strategy interface.
               In our example: Strategy interface: Sorter
               Strategy objects: PR_Queue,

               """
        return self._strategy


    def strategy(self, sorter: Sorter) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """
        self._sorter = sorter


    def sort(self, seq:list):
        return self._sorter.sort(seq)  # delegation



if __name__ == "__main__":

    l1 = [random.randint(0, 100) for i in range(50)]
    print("Before: ", l1)
    
    while True:
        print("\nMenu:")
        print("1. Display list")
        print("2. Shuffle list")
        print("3. Sort using Heap Priority Queue (PR_Queue)")
        print("4. Sort using Selection Sort with Unsorted Priority Queue")
        print("5. Sort using Insertion Sort with Sorted Priority Queue")
        print("6. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Current list:", l1)
        
        elif choice == '2':
            random.shuffle(l1)
            print("List shuffled.")

        elif choice == '3':
            context = Context(SortingALgorithm.PR_Queue)
            sorted_lst = context.sort(l1)
            print("Sorted list (Heap Priority Queue): ", sorted_lst)

        elif choice == '4':
            context = Context(SortingALgorithm.UnSortedPriorityQueue)
            sorted_lst = context.sort(l1)
            print("Sorted list (Selection Sort, Unsorted Priority Queue): ", sorted_lst)

        elif choice == '5':
            context = Context(SortingALgorithm.SortedPriorityQueue)
            sorted_lst = context.sort(l1)
            print("Sorted list (Insertion Sort, Sorted Priority Queue): ", sorted_lst)

        elif choice == '6':
            print("Exited Program")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")