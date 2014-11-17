from Tkinter import *


class Painter(Frame):

    CANVAS_HEIGHT = 400
    CANVAS_WIDTH = 500
    CANVAS_PADDING = 20
    LINK_LEN = 40
    MATRIX_DIMENSION = 0.50 * CANVAS_HEIGHT
    ARM_STAND_HEIGHT = 100
    ARM_LENGTH = 100
    BAR_THICKNESS = 20
    TIP_SPACE = 30
    TABLE_LEVEL = MATRIX_DIMENSION + 50
    TABLE_THICKNESS = 30
    TABLE_LENGTH = CANVAS_WIDTH - CANVAS_PADDING - 20
    ARM_SUPPORT_LENGTH = 50
    MATRIX_X1 = 50 + CANVAS_PADDING
    MATRIX_Y1 = BAR_THICKNESS * 0.75 + CANVAS_PADDING + 10 + LINK_LEN

    def __init__(self, parent, title, x, y, z):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title(title)
        self.box1 = x
        self.box2 = y
        self.box3 = z
        self.box = ["", "", ""]
        self.box_color = ["#fb0", "#f50", "blue"]
        self.arm_x = ""
        self.arm_y = ""
        self.claw_bar = ""
        self.left_claw = ""
        self.right_claw = ""
        self.claw = [self.left_claw, self.right_claw]
        self.arm_x_coords = []
        self.arm_y_coords = []
        self.claw_coords = []
        self.canvas = Canvas(self.parent, height=str(self.CANVAS_HEIGHT),
                width=str(self.CANVAS_WIDTH), bg='cyan')
        self.canvas.pack()
        self.draw()
        self.make_prompt()
        #coords = self.get_coords(self.box2)

        #print coords
        #self.move_item_to(self.box[2], coords)
        #time.sleep(1.0)
        #self.canvas.update_idletasks()
        #self.stretch_arm((coords[0] + coords[2]) / 2 + 5)
        #time.sleep(1.0)
        #self.canvas.update_idletasks()
        #self.lower_arm(coords[1] - 10)
        #self.canvas.update_idletasks()
        #self.stretch_arm(200)
        #self.follow_claw(self.box[2])
        #print self.box1.pos
        #print self.box2.pos
        #print self.box3.pos

    def get_coords(self, box):
        print("pos", box.pos)
        y1 = self.TABLE_LEVEL - ((box.pos[0] - 2) * 40)
        y2 = y1 - 40
        x1 = self.MATRIX_X1 + (box.pos[1] * 50)
        x2 = x1 + 40
        return [x1, y2, x2, y1]

    def get_coords_by_pos(self, pos):

        y1 = self.TABLE_LEVEL - ((pos[0] - 2) * 40)
        y2 = y1 - 40
        x1 = self.MATRIX_X1 + (pos[1] * 50)
        x2 = x1 + 40
        return [x1, y2, x2, y1]

    def move_item_to(self, item, new_coords):
        coords = self.canvas.coords(item)
        self.canvas.coords(item, new_coords[0], new_coords[1],
                             new_coords[2], new_coords[3])

    def stretch_arm(self, new_x):
        coords = self.canvas.coords(self.arm_x)
        coords[0] = new_x
        self.move_item_to(self.arm_x, coords)
        self.arm_x_coords = self.canvas.coords(self.arm_x)
        self.after_effect_x()

    def lower_arm(self, new_y):
        coords = self.canvas.coords(self.arm_y)
        coords[3] = new_y
        self.move_item_to(self.arm_y, coords)
        self.arm_y_coords = self.canvas.coords(self.arm_y)
        self.after_effect_y()

    def after_effect_x(self):
        y = 0.5 * (2 * self.CANVAS_PADDING + 20 + self.BAR_THICKNESS * 0.75)
        y1 = self.arm_x_coords[1]
        x1 = self.arm_x_coords[0]
        x2 = x1 - 10
        y2 = self.arm_x_coords[1] + self.LINK_LEN
        self.canvas.coords(self.arm_y, x2, y1, x1, y2)
        self.arm_y_coords = self.canvas.coords(self.arm_y)

        x = 0.5 * (2 * (self.arm_x_coords[0]) - 10)
        x1 = x - 25
        x2 = x + 25
        y1 = self.arm_x_coords[1] + self.LINK_LEN
        y2 = y1 + 5
        self.canvas.coords(self.claw_bar, x1, y1, x2, y2)

        c = self.claw
        y1 = y2
        y2 = y1 + self.LINK_LEN
        for i in range(2):
            x1 = x - 25 + (i * 50)
            x2 = x1 + 5 - (i * 10)
            self.canvas.coords(c[i], x1, y1, x2, y2)

        ax2 = x - 20
        bx2 = x + 20
        self.claw_coords = [ax2, y1, bx2, y2]

    def after_effect_y(self):
        self.arm_y_coords = self.canvas.coords(self.arm_y)
        x2, y1, x1, y2 = self.arm_y_coords

        x = 0.5 * (x1 + x2)
        x1 = x - 25
        x2 = x + 25
        y1 = y2
        y2 = y1 + 5
        self.canvas.coords(self.claw_bar, x1, y1, x2, y2)

        c = self.claw
        y1 = y2
        y2 = y1 + self.LINK_LEN
        for i in range(2):
            x1 = x - 25 + (i * 50)
            x2 = x1 + 5 - (i * 10)
            self.canvas.coords(c[i], x1, y1, x2, y2)

        cord1 = self.canvas.coords(c[0])
        cord2 = self.canvas.coords(c[1])

        ax2 = cord1[2]
        bx2 = cord2[0]
        self.claw_coords = [ax2, y1, bx2, y2]

    def follow_claw(self, item):
        self.move_item_to(item, self.claw_coords)

    def make_prompt(self):
        self.w = Entry(self.parent, width=40)
       # self.w.insert(0, '>>>')
        self.w.pack()
        btn = Button(self.parent, text='OK', command=self.act)
        btn.pack()

    def act(self):
        print(self.w.get())

    def draw(self):
        self.draw_table()
        self.draw_robot()
        self.draw_boxes()

    def draw_table(self):
        # some text

        self.canvas.create_text(60, 20, text='apoti_a-->yellow\n' +
                                             'apoti_b-->orange\n' +
                                             'apoti_d-->blue')

        x1 = 20 + self.CANVAS_PADDING
        x2 = self.TABLE_LENGTH
        y1 = self.TABLE_LEVEL
        y2 = y1 + self.TABLE_THICKNESS
        y = 0.5 * (y1 + y2)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill='brown')
        self.canvas.create_line(x1, y, x2, y)

    def draw_boxes(self):
        y1 = self.TABLE_LEVEL
        y2 = y1 - 40

        for i in range(3):
            x1 = self.MATRIX_X1 + (i * 50)
            x2 = x1 + 40
            self.box[i] = self.canvas.create_rectangle(x1,
                            y1, x2, y2, fill=self.box_color[i])

    def draw_robot(self):
        # the stand
        x1 = self.TABLE_LENGTH - 10
        x2 = x1 - self.BAR_THICKNESS
        y1 = self.TABLE_LEVEL
        y2 = self.CANVAS_PADDING

        self.canvas.create_rectangle(x1, y1, x2, y2, fill='grey')

        #the arm
        x1 = self.TABLE_LENGTH - 5
        y2 = y1 + 5

        self.canvas.create_rectangle(x1, y1, x2, y2, fill='grey')

        x2 = x1 - self.BAR_THICKNESS - self.ARM_LENGTH
        y1 = self.CANVAS_PADDING + 10
        y2 = y1 + self.BAR_THICKNESS * 0.75

        self.canvas.create_rectangle(x1, y1, x2, y2, fill='grey')

        # the appendages
        y = 0.5 * (y1 + y2)
        x1 = x2
        x2 = x1 - 50
        y1 = y - 5
        y2 = y + 5

        self.arm_x = self.canvas.create_rectangle(x1, y1, x2, y2, fill='grey')
        self.arm_x_coords = self.canvas.coords(self.arm_x)

        x1 = self.arm_x_coords[0]
        x2 = x1 - 10
        y2 = y1 + self.LINK_LEN

        self.arm_y = self.canvas.create_rectangle(x1, y1, x2, y2, fill='grey')

        self.arm_y_coords = self.canvas.coords(self.arm_y)

        # the claw
        x = 0.5 * (2 * (self.arm_x_coords[0]) - 10)
        x1 = x - 25
        x2 = x + 25
        y1 = y2
        y2 = y1 + 5

        self.claw_bar = self.canvas.create_rectangle(x1, y1, x2, y2,
            fill='grey')

        c = self.claw
        y1 = y2
        y2 = y1 + self.LINK_LEN
        for i in range(2):
            x1 = x - 25 + (i * 50)
            x2 = x1 + 5 - (i * 10)
            c[i] = self.canvas.create_rectangle(x1, y1, x2, y2, fill='grey')

        ax2 = x - 20
        bx2 = x + 20
        self.claw_coords = [ax2, y1, bx2, y2]
