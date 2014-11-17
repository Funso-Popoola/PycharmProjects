class RobotArm():
    """
    The blueprint for the arm of the robot: implementing the basic functions
    """

    def __init__(self, name):
        self.name = name
        self.location = [0, 3]
        self.arm_free = True
        self.holding = None

    def arm_is_free(self):
        """
        :return: true if the arm of the robot is free
        """

        if self.arm_free:
            return True
        else:
            return False

    def grasp(self, box):
        """
        make the robot arm grasp a box given as the param
        :param box: the box to be grasp
        :return: None
        """
        self.holding = box
        self.arm_free = False

    def free(self):
        """
        release the object currently held
        :return: None
        """
        self.holding = None
        self.arm_free = True

    def move_to(self, x):
        """
        move the arm by specifying destination coordinate
        :param x: a list specifying the coordinate of the destination
        :return: None
        """
        self.location = [x.pos[0], x.pos[1]]

    def move_to_pos(self, position):
        """
        move the arm by specifying destination on matrix grid
        :param position: a list specifying the destination on matrix grid
        :return:None
        """
        self.location = position

    def place_on_table(self):
        """
        place the current box on the table
        :return: None
        """
        self.move_to_pos([3, 3])
        self.free()
