# height and depth
# height: is distance of root node to leaf node
#        or number of edges between root to leaf node
#        or number of levels between root and leaf node
#       root node height is 0 (same as level)

# depth: is distance of a particular node from root node
'''
https://s3.amazonaws.com/hr-assets/0/1527626088-807ca5fc63-treeDepthSample1.png
'''


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, child_data):
        current = self
        if child_data < current.data:
            if current.left:
                current.left.add_child(child_data)
            else:
                current.left = BinarySearchTree(child_data)

        elif child_data > current.data:
            if current.right:
                current.right.add_child(child_data)
            else:
                current.right = BinarySearchTree(child_data)

    def print_tree(self):
        current = self
        # left tree
        if current.left:
            current.left.print_tree()
        # root
        print(current.data)
        # right tree
        if current.right:
            current.right.print_tree()


def build_tree(elements):
    root_node = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root_node.add_child(elements[i])

    return root_node


def height_tree(root_node):
    if root_node is None:
        return -1

    height = max(height_tree(root_node.left), height_tree(root_node.right)) + 1

    return height


lis = [3, 2, 5, 1, 4, 6, 7]
root = build_tree(lis)

print(height_tree(root))
# root.print_tree()
