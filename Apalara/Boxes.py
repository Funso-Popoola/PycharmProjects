__author__ = 'funso'


class Box():

    def __init__(self, name):
        self.name = name
        self.pos = list()
        self.box_below = None
        self.box_above = None
        self.box_to_right = None
        self.box_to_left = None
        self.on_table = True

    def get_position(self, world):
        for i in range(3):
            for j in range(3):
                if(world.environ_mat[i][j] == self):
                    self.pos = [i, j]

    def is_on_table(self):
        if(self.pos[1] == 2):
            self.on_table = True
        else:
            self.on_table = False

    def assign_rel(self, world):
        self.get_position(world)
        self.box_below = None
        self.box_above = None
        self.box_to_right = None
        self.box_to_left = None
        mat = world.environ_mat
        i = self.pos[0]
        j = self.pos[1]
        if(i == 2):
            if(j > 0 and isinstance(mat[i][j - 1], Box)):
                self.box_to_left = mat[i][j - 1]
            if(j < 2 and isinstance(mat[i][j + 1], Box)):
                self.box_to_right = mat[i][j + 1]
        if(i < 2 and isinstance(mat[i + 1][j], Box)):
            self.box_below = mat[i + 1][j]
        if(i > 0 and isinstance(mat[i - 1][j], Box)):
            self.box_above = mat[i - 1][j]


