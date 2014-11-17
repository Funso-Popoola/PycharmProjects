__author__ = 'funso'


from Boxes import Box


class World():

    def __init__(self, name, arm, table, x, y, z):
        self.name = name
        self.robot_arm = arm
        self.table = table
        self.box1 = x
        self.box2 = y
        self.box3 = z
        mat = [self.box1, self.box2, self.box3]
        self.environ_mat = [[0, 0, 0], [0, 0, 0], mat]
        self.assign_rel()

    def assign_rel(self):
        """
        get each box aware of its world
        :return:None
        """
        self.box1.get_position(self)
        self.box2.get_position(self)
        self.box3.get_position(self)

        self.box1.assign_rel(self)
        self.box2.assign_rel(self)
        self.box3.assign_rel(self)

    def refresh_matrix(self):
        """
        update the matrix with the changes in the environment
        :return: None
        """
        pos_a = self.box1.pos
        pos_b = self.box2.pos
        pos_c = self.box3.pos
        mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        mat[pos_a[0]][pos_a[1]] = self.box1
        mat[pos_b[0]][pos_b[1]] = self.box2
        mat[pos_c[0]][pos_c[1]] = self.box3
        self.environ_mat = mat

    def on(self, x, y):
        """
        checks if a box is on top of the other
        :param x: the box supposed to be on the other
        :param y: the box supposed to be under the other
        :return: boolean
        """
        status = False
        if(x.box_below == y):
            status = True
        return status

    def under(self, x, y):
        status = False
        if(y.box_to_below == x):
            status = True
        return status

    def clear(self, x):
        """
        checks if the top of a box is free
        :param x: the box object
        :return: boolean
        """
        status = False
        if(x.box_above):
            status = True
        return status

    def on_table(self, x):
        """
        checks if a box is on table
        :param x: the box object
        :return: boolean
        """
        status = False
        if(x.on_table):
            status = True
        return status

    def on_left(self, x, y):
        """
        checks if a box is to the left of the other
        :param x: the box object supposed to be to the left of the other
        :param y: the reference box object
        :return: boolean
        """
        status = False
        if(y.box_to_left == x):
            status = True
        return status

    def on_right(self, x, y):
        status = False
        if(y.box_to_right == x):
            status = True
        return status

    def grasping(self, x):
        """
        validate the claim that the robot arm is grasping a box
        :param x: the box object supposed to be held
        :return: boolean
        """
        status = False
        if (self.robot_arm.holding == x):
            status = True
        return status


    def is_box(self, x):
        """
        validates that an object is a box
        :param x: the box in question
        :return: boolean
        """
        status = False
        if(isinstance(x, Box)):
            status = True
        return status


