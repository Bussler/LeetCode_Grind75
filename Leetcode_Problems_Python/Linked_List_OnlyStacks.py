
class MyQueue_OnlyStacks:

    def __init__(self):
        self.data = []
        

    def push(self, x: int) -> None:
        self.data.append(x)
        return None
        
    def pop(self) -> int:
        elem = self.data[0]
        del self.data[0]
        return elem
        
    def peek(self) -> int:
        return self.data[0]
        
    def empty(self) -> bool:
        return len(self.data) == 0
    

def test_Queue_OnlyStacks():
    obj = MyQueue_OnlyStacks()
    
    x = 10
    y = 12
    
    obj.push(x)
    param_2 = obj.pop()
    obj.push(y)
    param_3 = obj.peek()
    param_4 = obj.empty()
    
    
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()