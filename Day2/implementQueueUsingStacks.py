class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.out_stack:
            self.out_stack.append(x)
        else:
            self.in_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        ret = self.out_stack.pop()
        #loops through in_stack
        for _ in range(len(self.in_stack)-1):
            #appends value to out_stack
            self.out_stack.append(self.in_stack.pop())
        #sets in and out stack values
        self.in_stack, self.out_stack = self.out_stack, self.in_stack
                
        return ret

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.out_stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.in_stack and not self.out_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()