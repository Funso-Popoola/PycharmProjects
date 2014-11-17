__author__ = 'funso'


class BinTree():

    def __init__(self):
        self.root = None

    def pre_order_traverse(self, root):
        if (root == None):
            return
        self.visit(root)
        self.pre_order_traverse(root.get_left_child)
        self.pre_order_traverse(root.get_right_child)

    def in_order_traverse(self, root):
        if (root == None):
            return
        self.visit(root)
        self.in_order_traverse(root.get_left_child)
        self.in_order_traverse(root.get_right_child)

    def post_order_traverse(self, root):
        if (root == None):
            return
        self.visit(root)
        self.post_order_traverse(root.get_left_child)
        self.post_order_traverse(root.get_right_child)

    def visit(self, root):
        print(root.value)

    def insert(self, node):

        pass

    def remove(self, node):
        pass

    def find(self, node):
        curr = self.root
        while not curr.get_value() == node.get_value():
            if curr == None:
                return None
            elif node.get_value() > curr.get_value():
                curr = curr.get_right_child()
            elif node.get_value() < curr.get_value():
                curr = curr.get_left_child()

        return curr



