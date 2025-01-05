class Stack:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def Push(self, item):
        if not self.IsFull():
            self.items.append(item)
        else:
            raise Exception("Stack is full")

    def Pop(self):
        if not self.IsEmpty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")

    def TopItem(self):
        if not self.IsEmpty():
            return self.items[-1]
        return None

    def IsEmpty(self):
        return len(self.items) == 0

    def IsFull(self):
        return len(self.items) >= self.max_size

# 使用示例
stack = Stack(5)
stack.Push(1)
stack.Push(2)
stack.Push(3)
print(stack.TopItem())  # 輸出 3
print(stack.IsEmpty())  # 輸出 False
print(stack.IsFull())   # 輸出 False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
