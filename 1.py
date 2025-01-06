class Stack:
    def __init__(self, max_size):
        self.items = [] # 初始化一個空列表來儲存推疊中的元素
        self.max_size = max_size # 儲存推疊的最大容量

    def Push(self, item):
        if not self.IsFull(): # 如果推疊未滿
            self.items.append(item) # 將元素添加到推疊中
        else:
            raise Exception("Stack is full") # 如果推疊已滿，則引發異常

    def Pop(self): # 從推疊中移除並返回頂部的元素
        if not self.IsEmpty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")

    def TopItem(self):
        if not self.IsEmpty():
            return self.items[-1] # 返回頂部的元素，但不移除它
        return None

    def IsEmpty(self):
        return len(self.items) == 0

    def IsFull(self):
        return len(self.items) >= self.max_size # 如果推疊中的元素數量等於最大容量，則推疊已滿

# 使用示例
stack = Stack(5) # 創建一個最大容量為5的推疊
stack.Push(1)
stack.Push(2)
stack.Push(3)
stack.Push(4)
stack.Push(5)
"""
stack.Push(6)
這裡會引發異常，因為推疊已滿
"""
print(stack.TopItem()) # 輸出 5
print(stack.IsEmpty()) # 輸出 False
print(stack.IsFull())  # 輸出 True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
