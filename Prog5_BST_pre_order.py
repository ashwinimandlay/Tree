# binary search tree (BST)
# pre-order traversal
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def add_child(self, child_data):
        if child_data == self.data:
            return

        elif child_data < self.data:
            if self.left:
                self.left.add_child(child_data)
            else:
                self.left = BinaryTreeNode(child_data)
                self.left.parent = self

        else:
            if self.right:
                self.right.add_child(child_data)
            else:
                self.right = BinaryTreeNode(child_data)
                self.right.parent = self

    def pre_order_traversal(self):
        element = []
        # root node
        element.append(self.data)

        # left tree
        if self.left:
            element += self.left.pre_order_traversal()
        else:
            pass
        # right tree
        if self.right:
            element += self.right.pre_order_traversal()

        return element

    def print_binary_tree(self):
        print(' ' * 3 * self.node_level(), end='')
        print(self.data)
        # for left tree
        if self.left:
            self.left.print_binary_tree()
        else:
            return

        # for right tree
        if self.right:
            self.right.print_binary_tree()
        else:
            return

    def node_level(self):
        temp = self
        level = 0
        while temp.parent:
            temp = temp.parent
            level += 1
        return level


def build_tree(elements):
    root = BinaryTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


lis = [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]
root_node = build_tree(lis)

# root_node.print_binary_tree()

print(root_node.pre_order_traversal())
