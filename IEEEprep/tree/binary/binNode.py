__author__ = 'funso'


class BinNode():

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    def set_left_child(self, left_child):
        self.left_child = left_child

    def get_left_child(self):
        return self.left_child

    def set_right_child(self, right_child):
        self.right_child = right_child

    def get_right_child(self):
        return self.right_child

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

