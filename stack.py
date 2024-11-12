class Stack:
    """first in last out"""
    def __init__(self) -> None:
        self.stack = []
        self.min_nums = []
    def push(self,num):
        self.stack.append(num)
        if not(self.min_nums) or self.min_nums[-1] <= num:
            self.min_nums.append(num)
    def pop(self):
        return_value =  self.stack.pop()
        if return_value == self.min_nums[-1]:
            self.min_nums.pop()
        return return_value
    def top(self):
        num_to_return = self.stack[-1]
        return num_to_return
    def min(self):
        return self.min_nums[-1]
goida = Stack()
goida.push(52)
goida.push(62)
print(goida.min(),goida.top(),goida.pop(),goida.top())