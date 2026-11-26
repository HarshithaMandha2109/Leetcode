class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minstack or value<=self.minstack[-1]:
            self.minstack.append(value)
        

    def pop(self) -> None:
        # if self.top==1:
        #     return None
        ele=self.stack.pop()
        if self.minstack[-1]==ele:
            self.minstack.pop()
        

    def top(self) -> int:
        # if self.top==1:
        #     return None
        return self.stack[-1]

        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()