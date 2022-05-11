# trees intro
# manually adding nodes
"""
    Electronics
        |__Phones
            |__android
            |__iphone
        |__laptops
            |__Mac
            |__Asus
            |__HP
            |__Lenovo
        |__Tv
            |__Samsung
            |__LG
            |__Oneplus
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print('  ' * 2 * self.levels(), '|__', end='')
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def levels(self):
        temp = self
        level = 0
        while temp.parent:
            temp = temp.parent
            level += 1
        return level


def build_product_tree():
    root = TreeNode('Electronics')

    phones = TreeNode('Phones')
    phones.add_child(TreeNode('android'))
    phones.add_child(TreeNode('iphone'))

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Asus'))
    laptop.add_child(TreeNode('HP'))
    laptop.add_child(TreeNode('Lenovo'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('OnePlus'))

    root.add_child(phones)
    root.add_child(laptop)
    root.add_child(tv)

    # returning root is necessary for print_tree func
    # otherwise can be skipped
    return root


root_of_tree = build_product_tree()
root_of_tree.print_tree()
