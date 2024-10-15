'''
Implement a function that splits a given queue into two halves, upper half and lower half. The function then returns the two queues.

The given queue should not be lost. If the queue size is odd, the upper half will have one element more than the lower half.
'''

from array_queue import ArrayQueue

def printQueue(q):
    tempQ = ArrayQueue()
    while not q.is_empty():
       tempQ.enqueue(q.first())
       print(q.dequeue(), end = ' ') 
    while not tempQ.is_empty():
        q.enqueue(tempQ.dequeue())
        
    print()
    

def splitQueue(queue):
    
    n = len(queue)              # Gets the size of queue
    firstHalf = ArrayQueue()    # Makes a new queue
    secondHalf = ArrayQueue()   # Makes a new queue
    halfway = n // 2            # Calculate halfway
    
    if n % 2 == 1:
        halfway += 1            # Add 1 to halfway if n is odd so that first queue has more elements
    
    for _ in range(halfway):
        firstHalf.enqueue(queue.first())    # Add first element from 'queue' to firstHalf
        queue.enqueue(queue.dequeue())      # Move that first element to the back to make way for second element
    
    for _ in range(halfway+1, n+1):
        secondHalf.enqueue(queue.first())   # Adds remaning elements from 'queue' to firstHalf
        queue.enqueue(queue.dequeue())      # Move added elements to the back to restore the original given queue
    
    return firstHalf, secondHalf

if __name__ == '__main__':
    q = ArrayQueue()

    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    q.enqueue('d')
    q.enqueue('e')

    q1,q2 = splitQueue(q)

    print("original: ", end = ' '); 
    printQueue(q)

    print("q1: ", end = ' '); 
    printQueue(q1)

    print("q2: ", end = ' '); 
    printQueue(q2)