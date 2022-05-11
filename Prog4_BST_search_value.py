# binary search tree (BST)
# search a number or value
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, child_data):
        if child_data == self.data:
            return

        elif child_data < self.data:
            if self.left:
                self.left.add_child(child_data)
            else:
                self.left = BinarySearchTree(child_data)

        else:
            if self.right:
                self.right.add_child(child_data)
            else:
                self.right = BinarySearchTree(child_data)

    def search_in_tree(self, value):
        if value == self.data:
            return True

        elif value < self.data:
            if self.left:
                return self.left.search_in_tree(value)
            else:
                return False

        else:
            if self.right:
                return self.right.search_in_tree(value)
            else:
                return False


def build_binary_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


lis = [4, 2, 8, 0, 3, 5, 9]
root_node = build_binary_tree(lis)

print(root_node.search_in_tree(1))
