class Node:
  def __init__(self, value):
    self.value=Value
    self.left=None
    self.right=None
class BinaryTree:
  def __init__(self):
    self.root=None
  def insert(self, value):
    new=Node(value)
    if self.root is None:
      self.root=new
      return