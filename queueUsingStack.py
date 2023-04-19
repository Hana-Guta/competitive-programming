class MyQueue:
    
    def __init__(self):
        self.front = []
        self.back = []
    def push(self, x: int) -> None:
        self.front.append(x)
    def pop(self) -> int:
        if not self.back:
            self.fill()
        return self.back.pop()

    def peek(self) -> int:
        if not self.back:
            self.fill()
        temp = self.back.pop()
        self.back.append(temp)
        return temp
    
    def empty(self) -> bool:
        return not len(self.back) and not len(self.front)

    
    def fill(self):
        while self.front:
            self.back.append(self.front.pop())
