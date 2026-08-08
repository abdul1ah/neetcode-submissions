class MyStack:

    def __init__(self):
        self.list1 = []
        self.list2 = []
        self.top_val = None
        

    def push(self, x: int) -> None:
        self.list1.append(x)
        self.top_val = x

    def pop(self) -> int:

        while len(self.list1) > 1:
            self.top_val = self.list1.pop(0)
            self.list2.append(self.top_val)
        
        removed = self.list1.pop(0)
        self.list1 , self.list2 = self.list2 , self.list1
        return removed

    def top(self) -> int:

        return self.top_val
        

    def empty(self) -> bool:
        return len(self.list1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()