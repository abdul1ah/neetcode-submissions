class MyQueue:

    def __init__(self):
        self.insert=[]
        self.remove=[]

    def push(self, x: int) -> None:
        self.insert.append(x)

    def pop(self) -> int:
        removed=None
        if not self.remove:
            while self.insert:
                to_insert = self.insert.pop()
                self.remove.append(to_insert)
        removed = self.remove.pop()
        return removed

    def peek(self) -> int:
        top=None
        if not self.remove:
            while self.insert:
                to_insert = self.insert.pop()
                self.remove.append(to_insert)
        return self.remove[-1]

    def empty(self) -> bool:
        return not self.insert and not self.remove

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()