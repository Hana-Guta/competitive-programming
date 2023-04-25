class MinStack:

    def __init__(self):
        self.obj = []
        
    def push(self, val: int) -> None:
        self.obj.append(val)

    def pop(self) -> None:
        if len(self.obj) == 0:
            return "the stack is empty"
        return self.obj.pop()

    def top(self) -> int:
         if len(self.obj) == 0:
            return "the stack is empty"
         return self.obj[-1]

    def getMin(self) -> int:
        return min(self.obj)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
