from collections import deque
class Deque:
    def __init__(self):
        self.dq=deque()
    def addFront(self, value):
        self.dq.appendleft(value)
        print(f"AddFront {value} -> {list(self.dq)}")
    def addRear(self, value):
        self.dq.append(value)
        print(f"AddRear {value} -> {list(self.dq)}")
    def removeFront(self):
        if self.isEmpty():return "Empty!"
        val=self.dq.popleft()
        print(f"RemoveFront {val} -> {list(self.dq)}")
    def removeRear(self):
        if self.isEmpty():return "Empty!"
        val=self.dq.pop()
        print(f"RemoveRear {val} -> {list(self.dq)}")
        return val
    def peekFront(self):
      return self.dq[0] if not self.isEmpty() else "Empty!"
    def peekRear(self):
        return self.dq[-1] if not self.isEmpty() else "Empty!"
    def isEmpty(self):
      return len(self.dq) == 0
    def size(self):
      return len(self.dq)
d=Deque()
d.addFront(1)
d.addFront(2)
d.addFront(3)
d.addRear(4)
d.addRear(5)
d.addRear(6)
d.removeFront()
d.removeRear()

    