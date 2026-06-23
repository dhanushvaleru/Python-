import heapq
class PriorityQueue:
  def __init__(self):
    self.heap = []
    self.counter = 0
  def insert(self, item, priority):
    heapq.heappush(self.heap, (-priority, self.counter, item))
    self.counter += 1
    print(f"Inserted '{item}' with priority {priority}")
  def extractMin(self):
    if not self.isEmpty():
      priority, _, item = heapq.heappop(self.heap)
      print(f"Extracted '{item}' with priority {priority}")
      return item
  def peek(self):
    return self.heap[0][2] if not self.isEmpty() else "Empty"
  def isEmpty(self):
    return len(self.heap) == 0
  def size(self):
    return len(self.heap)
pq = PriorityQueue()
pq.insert("A", 3)
pq.insert("B", 1)
pq.insert("C", 2)
pq.insert("D",4)
pq.extractMin()
print(pq.peek())
print(pq.isEmpty())
print(pq.size())