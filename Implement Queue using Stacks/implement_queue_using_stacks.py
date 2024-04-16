"""
Implement Queue using Stacks.
"""
class Node:
    """
    Node class.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """
    Stack class.
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Check if stack is empty.
        """
        return self.head is None

    def push(self, data):
        """
        Push element to stack.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """
        Pop element from stack.
        """
        popped = self.head.data
        self.head = self.head.next
        return popped

    def peek(self):
        """
        Peek stack.
        """
        return self.head.data

class MyQueue:
    """
    MyQueue class.
    """
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        """
        Push to stack.
        """
        self.stack1.push(x)

    def pop(self) -> int:
        """
        Pop from stack.
        """
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Peek stack.
        """
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self) -> bool:
        """
        Check if stack is empty.
        """
        return self.stack1.is_empty() and self.stack2.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
