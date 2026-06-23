class  Node:
  def __init__(self, data):
    self.data=data
    self.next=None
class SinglyLinkedList:
  def __init__(self):
    self.head=None
  def insertAtEnd(self, data):
    node=Node(data)
    if not self.head: self.head = node; return
    cur = self.head
    while cur.next: cur = cur.next
    cur.next = node
  def insertAtStart(self, data):
    node = Node(data)
    node.next = self.head: self.head = node
  def insertAtPos(self, data, pos):
    if pos == 0: self.insertAtStart(data); 
    return node, cur, i = Node(data), self.head, 0
    while cur and i < pos-1: cur = cur.next, i+=1
    if  cur: node.next = cur.next; cur.next = node