class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
        print(f"Pushed: {value} | Stack: {self.stack}")
    def pop(self):
        if self.isEmpty():
            return "Stack Underflow!"
        val=self.stack.pop()
        print(f"Popped: {val} | Stack: {self.stack}")
        return val
    def peek(self):
        if self.isEmpty():
            return "Stack is empty!"
        return self.stack[-1]  
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    def display(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            print("TOP ->",self.stack[::-1])
stack=Stack()
stack.push(10); stack.push(20); stack.push(30)
print("Peek:",stack.peek())
stack.pop()
print("size:",stack.size())
stack.display()