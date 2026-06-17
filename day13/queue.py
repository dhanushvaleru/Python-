class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def peekfront(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def peekrear(self):
        if not self.is_empty():
           return self.queue[-1]
        return None
    def is_empty(self):
        return self.queue==0
    def clear(self):
        self.queue=[]
d = queue()
d.enqueue(10)
d.enqueue(20)
d.enqueue(30)
d.enqueue(40)
d.enqueue(50)
print(d.dequeue())
print(d.peekfront())
print(d.peekrear())
print(d.is_empty())
d.clear()
print(d.is_empty())