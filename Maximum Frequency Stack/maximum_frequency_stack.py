"""
Maximum Frequency Stack script.
"""
from collections import defaultdict, deque

class FreqStack:
    """
    FreqStack class.
    """
    def __init__(self):
        self.freq = defaultdict(int)
        self.stack = defaultdict(deque)

    def push(self, val: int) -> None:
        """
        Push to stack.
        """
        freq = self.freq[val] + 1
        self.freq[val] = freq
        self.stack[freq].append(val)

    def pop(self) -> int:
        """
        Pop from stack.
        """
        max_freq = max(self.freq.values())
        val = self.stack[max_freq].pop()
        if not self.stack[max_freq]:
            del self.stack[max_freq]
        self.freq[val] -= 1
        if self.freq[val] == 0:
            del self.freq[val]
        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
