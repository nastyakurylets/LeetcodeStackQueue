"""
Implement Stack using Queues script.
"""
class Node:
    """
    Node class.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """
    Queue class.
    """
    def __init__(self):
        self.front = None
        self.back = None

    def is_empty(self):
        """
        Check if queue is empty.
        """
        return self.front is None

    def enqueue(self, data):
        """
        Add a new element to the end of the queue.
        """
        new_node = Node(data)
        if self.back is None:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        """
        Remove and return an element from the beginning of the queue.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.front.data
        if self.front == self.back:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next
        return data

    def peek(self):
        """
        Peek queue.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

class MyStack:
    """
    MyStack class.
    """
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        """
        Push to queue.
        """
        self.q2.enqueue(x)
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """
        Pop from queue.
        """
        return self.q1.dequeue()

    def top(self) -> int:
        """
        Returns the value of the top element of the stack without removing it.
        """
        return self.q1.peek()

    def empty(self) -> bool:
        """
        Check if queue is empty.
        """
        return self.q1.is_empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
