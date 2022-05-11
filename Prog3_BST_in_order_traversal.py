# binary search tree (BST)
# in_order = (left, root, right)
# pre_order = (root, left, right)
# post_order = (left, right, root)
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, child_data):
        if self.data == child_data:
            return

        elif child_data < self.data:
            if self.left:
                self.left.add_child(child_data)
            else:
                self.left = BinarySearchTreeNode(child_data)

        else:
            if self.right:
                self.right.add_child(child_data)
            else:
                self.right = BinarySearchTreeNode(child_data)

    def traverse_in_order(self):
        element = []
        if self.left:
            element += self.left.traverse_in_order()

        element.append(self.data)

        if self.right:
            element += self.right.traverse_in_order()

        return element


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


lis = [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]
root_node = build_tree(lis)

# traversal will basically sort in increasing order and
# note that each node must be unique 
print(root_node.traverse_in_order())

# this can also be used to sort string in increasing order
lis1 = ['india', 'usa', 'canada', 'india', 'usa', 'uk', 'canada']
root_node_country = build_tree(lis1)

# unique nodes are only considered (sets logic)
print(root_node_country.traverse_in_order())
