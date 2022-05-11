# hacker rank method of building tree
# 2 classes required (like in linked node)
# no build_tree() function will be required

# if we make two classes then recursion will not be possible
# so all the functions such as print_tree() and ssearch_tree()
# we have to define them outside both our class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_child(self, child_value):
        if self.root is None:
            self.root = Node(child_value)
        else:
            current = self.root

            while True:
                if child_value < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(child_value)
                        break

                elif child_value > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(child_value)
                        break
                # this else is for child_value == current.data
                else:
                    break
    """
    # if we define function inside this class then we cannot
    # use recursion as current.left is a node class and node 
    # doesn't have print_tree_inorder() function
    
    # so it is easier to call it outside of class then our 
    # print function will be independent of class and then
    # we can easily use recursion"""

    # def print_tree_inorder(self):
    #     current = self.root
    #     # left
    #     if current.left:
    #         current.left.print_tree_inorder()
    #     # root
    #     print(current.data)
    #     # right
    #     if current.right:
    #         current.right.print_tree_inorder()


def preorder(root):
    # Write your code here
    print(root.data, end=' ')

    if root.left:
        preorder(root.left)

    if root.right:
        preorder(root.right)


lis = [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]
tree = BinaryTree()
for children in lis:
    tree.add_child(children)

preorder(tree.root)
