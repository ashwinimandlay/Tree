# binary tree
# at most two children
class Node:
    def __init__(self, node_value):
        self.node_value = node_value
        self.left = None
        self.right = None


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(7)
"""
             1
          /      \
        2          3
       /  \       /  \
      7   None  None  None
    /   \
  None  None
"""
