import Tkinter
import time
import ttk
from Tkinter import *


import RobotArm
from Boxes import Box
from RobotArm import RobotArm as Robot_arm
from World import World
from Painter import Painter
from Table import Table

global apalara
apalara = Robot_arm('apalara')
apoti_a = Box('apoti_a')
apoti_b = Box('apoti_b')
apoti_d = Box('apoti_d')
global apoti
apoti = [apoti_a, apoti_b, apoti_d]
tabili = Table('tabili', apoti_a, apoti_b, apoti_d)
global aye
aye = World('aye', apalara, tabili, apoti_a, apoti_b, apoti_d)
itumo = {'apoti_a': apoti_a, 'apoti_b': apoti_b, 'apoti_d': apoti_d}
onka = {'apoti_a': 0, 'apoti_b': 1, 'apoti_d': 2}
root = Tk()
global ayaworan
ayaworan = Painter(root, 'Apalara', apoti_a, apoti_b, apoti_d)


def swap(x, y):
    if(x.box_above is None or y.box_above is None):

        apalara.free()
        coords = ayaworan.get_coords(y)
        temp_coords = list(coords)
        apalara.move_to(y)
        ayaworan.stretch_arm((coords[0] + coords[2]) / 2 + 5)
        ayaworan.lower_arm(coords[1] - 5)
        apalara.grasp(y)
        coords = ayaworan.get_coords_by_pos([6, 3])

        ayaworan.stretch_arm((coords[0] + coords[2]) / 2 + 5)
        i = onka.get(y.name)
        ayaworan.follow_claw(ayaworan.box[i])
        ayaworan.lower_arm(coords[1] - 5)
        ayaworan.follow_claw(ayaworan.box[i])

        coords = ayaworan.get_coords_by_pos([2, 3])
        ayaworan.stretch_arm((coords[0] + coords[2]) / 2 + 5)
        ayaworan.follow_claw(ayaworan.box[i])
        ayaworan.lower_arm(coords[1] - 5)
        ayaworan.follow_claw(ayaworan.box[i])

        apalara.free()

        coords = ayaworan.get_coords_by_pos([6, 3])
        ayaworan.stretch_arm((coords[0] + coords[2]) / 2 + 5)
        ayaworan.lower_arm(coords[1] - 5)

        coords = ayaworan.get_coords(x)
        temporal = list(coords)
        apalara.move_to(x)
        ayaworan.stretch_arm((coords[0] + coords[2]) / 2 + 5)
        ayaworan.lower_arm(coords[1] - 5)
        apalara.grasp(x)

        coords = ayaworan.get_coords_by_pos([6, 3])

        ayaworan.stretch_arm((coords[0] + coords[2]) / 2 + 5)
        i = onka.get(x.name)
        ayaworan.follow_claw(ayaworan.box[i])
        ayaworan.lower_arm(coords[1] - 5)
        ayaworan.follow_claw(ayaworan.box[i])

        ayaworan.stretch_arm((temp_coords[0] + temp_coords[2]) / 2 + 5)
        ayaworan.follow_claw(ayaworan.box[i])
        ayaworan.lower_arm(temp_coords[1] - 5)
        ayaworan.follow_claw(ayaworan.box[i])

        apalara.free()

        coords = ayaworan.get_coords_by_pos([6, 3])
        ayaworan.stretch_arm((coords[0] + coords[2]) / 2 + 5)
        ayaworan.lower_arm(coords[1] - 5)

        coords = ayaworan.get_coords(y)
        apalara.move_to(y)
        ayaworan.stretch_arm((coords[0] + coords[2]) / 2 + 5)
        ayaworan.lower_arm(coords[1] - 5)
        apalara.grasp(y)

        coords = ayaworan.get_coords_by_pos([6, 3])

        ayaworan.stretch_arm((coords[0] + coords[2]) / 2 + 5)
        i = onka.get(y.name)
        ayaworan.follow_claw(ayaworan.box[i])
        ayaworan.lower_arm(coords[1] - 5)
        ayaworan.follow_claw(ayaworan.box[i])

        ayaworan.stretch_arm((temp_coords[0] + temp_coords[2]) / 2 + 5)
        ayaworan.follow_claw(ayaworan.box[i])
        ayaworan.lower_arm(temp_coords[1] - 5)
        ayaworan.follow_claw(ayaworan.box[i])

        apalara.free()

        x.pos, y.pos = y.pos, x.pos

    else:
        print " impossible "


def place_under(x, y):
    #placing x under y
    if(y.pos[0] > 0):
        x.pos = list(y.pos)
        y.pos[0] -= 1
    else:
        print"impossible"


def place_on_top(x, y):
    #placing x on top of y
    if(y.pos[0] > 0):
        x.pos = [y.pos[0] - 1, y.pos[1]]
    else:
        print "impossible"


def stack_all_on(x, other1, other2):
    aye.assign_rel()
    if(x.pos[0] == 2):
        other1.pos = [x.pos[0] - 1, x.pos[1]]
        other2.pos = [x.pos[0] - 2, x.pos[1]]
    else:
        print"impossible"


def redraw():
    for each in apoti:
        coords = ayaworan.get_coords(each)
        ayaworan.move_item_to(each, coords)


def print_mat():
    for item in aye.environ_mat:
        for each in item:
            if(isinstance(each, Box)):
                print each.name,
            else:
                print each,
        print ""


def no_gui():
    option = int(raw_input("Enter your choice:"))
    if (option == 1):
        operand = raw_input("The boxes to swap:")
        boxes = operand.split(" ")
        if(len(boxes) == 3):
            x = itumo.get(boxes[0])
            y = itumo.get(boxes[2])
            swap(x, y)
            aye.refresh_matrix()
            print_mat()

    elif(option == 2):
        operand = raw_input("Which box under which:")
        boxes = operand.split(" ")
        if(len(boxes) == 3):
            x = itumo.get(boxes[0])
            y = itumo.get(boxes[2])
            place_under(x, y)
            aye.refresh_matrix()
            print_mat()

    elif(option == 3):
        operand = raw_input("Which box on top of which:")
        boxes = operand.split(" ")
        if(len(boxes) == 3):
            x = itumo.get(boxes[0])
            y = itumo.get(boxes[2])
            print x.pos, y.pos
            place_on_top(x, y)
            print x.pos, y.pos
            aye.refresh_matrix()
            print_mat()

    elif(option == 4):
        operand = raw_input("The box to stack others on:")
        boxes = operand.split(" ")
        if(len(boxes) == 1):
            x = itumo.get(boxes[0])
            print apoti
            others = list(apoti)
            others.remove(x)
            print x
            print others
            stack_all_on(x, others[0], others[1])
            aye.refresh_matrix()
            print_mat()

    else:
        print "invalid command"


def paint():
    swap(apoti[1], apoti[0])
    ayaworan.mainloop()


if __name__ == '__main__':
    #main()
    #paint()
    print_mat()
    print ("1. Swap any two boxes \n"
         + "2. Place a box under another box \n"
         + "3. Place a box on top of another \n"
         + "4. Stack all the boxes on one box \n")
    while (True):
        no_gui()