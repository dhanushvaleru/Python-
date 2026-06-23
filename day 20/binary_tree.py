class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None
class BinaryTree:
    # A plain binary tree: each node has at most two
    # children, with NO ordering rule. Insertion fills
    # the tree level by level (left to right).
    def __init__(self):
        self.root = None
    def insert(self, value):
        new = Node(value)
        if self.root is None:
            self.root = new
            return
        queue = [self.root]            # level-order fill
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = new;  return
            queue.append(node.left)
            if node.right is None:
                node.right = new; return
            queue.append(node.right)
    def preorder(self, node, out=None):
            # root -> left -> right
            if out is None: out = []
            if node:
                out.append(node.value)
                self.preorder(node.left,  out)
                self.preorder(node.right, out)
            return out
    def postorder(self, node, out=None):
            #   left -> right -> root
            if out is None: out = []
            if node:
                self.postorder(node.left,  out)
                self.postorder(node.right, out)
                out.append(node.value)
            return out
    def inorder(self, node, out=None):
            #  left -> root -> right
            if out is None: out = []
            if node:
                self.inorder(node.left,out)
                out.append(node.value)
                self.inorder(node.right,  out) 
            return out
# --- Using it ---
bt = BinaryTree()
for v in [1,2,3,4,5,6,7]:
    bt.insert(v)
print(bt.inorder(bt.root))
print(bt.preorder(bt.root))
print(bt.postorder(bt.root))