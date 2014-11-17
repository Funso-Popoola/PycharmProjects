__author__ = 'funso'


exa = {'0': 0,'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}
register = []
labelled_i = {}
comp_res = ""
next_i = ""
for i in range(16):
    temp = []
    for j in range(16):
        temp.append('00')
    register.append(temp)

next_i = None

def prt (a1, a2 = None):
    addr1 = str(a1)
    start_i = exa.get(addr1[0])
    start_j = exa.get(addr1[1])
    if ( a2 == None):
        a2 = a1
    addr2 = str(a2)
    end_i = exa.get(addr2[0])
    end_j = exa.get(addr2[1])
    for i in range(start_i, end_i + 1):
        for j in range(start_j, end_j + 1):
            num1 = register[i][j]
            print str(num1),
    print ""


def move_n_a (number, memory_loc):
    addr = str(memory_loc)
    register[exa.get(addr[0])][exa.get(addr[1])] = number

def move_n_da (number, reg):
    addr = str(reg)
    move_n_a(number, register[exa.get(addr[0])][exa.get(addr[1])])

def move_da_a (deref, memory):
    addr = str(deref)
    numb = register[exa.get(addr[0])][exa.get(addr[1])]
    move_a_a(numb, memory)

def move_da_da(fro , to):
    addr = str(fro)
    new_addr = register[exa.get(addr[0])][exa.get(addr[1])]
    move_a_da(new_addr, to)

def move_a_da(here, there):
    fro_addr = str(here)
    to_addr = str(there)
    to_addr = register[exa.get(to_addr[0])][exa.get(to_addr[1])]
    register[exa.get(to_addr[0])][exa.get(to_addr[1])] = register[exa.get(fro_addr[0])][exa.get(fro_addr[1])]

def move_a_a(here, there):
    fro_addr = str(here)
    to_addr = str(there)
    register[exa.get(to_addr[0])][exa.get(to_addr[1])] = register[exa.get(fro_addr[0])][exa.get(fro_addr[1])]

def add(x, y, z):
    return str(hex((int(str(x), 16) + (int(str(y), 16) * z)) % 256)).upper()[2:]

def add_n(n, b):
    addr_b = str(b)
    register[exa.get(addr_b[0])][exa.get(addr_b[1])] = add(register[exa.get(addr_b[0])][exa.get(addr_b[1])], n, 1)

def add_a(b, a):
    addr_a = str(a)
    addr_b = str(b)
    register[exa.get(addr_a[0])][exa.get(addr_a[1])] = add(register[exa.get(addr_b[0])][exa.get(addr_b[1])], register[exa.get(addr_a[0])][exa.get(addr_a[1])], 1)

def sub_n(n, b):
    addr_b = str(b)
    register[exa.get(addr_b[0])][exa.get(addr_b[1])] = add(register[exa.get(addr_b[0])][exa.get(addr_b[1])], n, -1)

def sub_a(b, a):
    addr_a = str(a)
    addr_b = str(b)
    register[exa.get(addr_a[0])][exa.get(addr_a[1])] = add(register[exa.get(addr_b[0])][exa.get(addr_b[1])], register[exa.get(addr_a[0])][exa.get(addr_a[1])], -1)

def and_n(n, b):
    addr_b = str(b)
    register[exa.get(addr_b[0])][exa.get(addr_b[1])] = n and register[exa.get(addr_b[0])][exa.get(addr_b[1])]

def and_a(b, a):
    addr_a = str(a)
    addr_b = str(b)
    register[exa.get(addr_a[0])][exa.get(addr_a[1])] = register[exa.get(addr_a[0])][exa.get(addr_a[1])] and register[exa.get(addr_b[0])][exa.get(addr_b[1])]

def or_n(n, b):
    addr_b = str(b)
    register[exa.get(addr_b[0])][exa.get(addr_b[1])] = n or register[exa.get(addr_b[0])][exa.get(addr_b[1])]

def or_a(b, a):
    addr_a = str(a)
    addr_b = str(b)
    register[exa.get(addr_a[0])][exa.get(addr_a[1])] = register[exa.get(addr_a[0])][exa.get(addr_a[1])] or register[exa.get(addr_b[0])][exa.get(addr_b[1])]

def xor_n(n, b):
    addr_b = str(b)
    register[exa.get(addr_b[0])][exa.get(addr_b[1])] = (n and ( not register[exa.get(addr_b[0])][exa.get(addr_b[1])])) or (not n and ( register[exa.get(addr_b[0])][exa.get(addr_b[1])]))

def xor_a(b, a):
    addr_a = str(a)
    addr_b = str(b)
    register[exa.get(addr_a[0])][exa.get(addr_a[1])] = (register[exa.get(addr_a[0])][exa.get(addr_a[1])] and (not register[exa.get(addr_b[0])][exa.get(addr_b[1])])) or (register[exa.get(addr_a[0])][exa.get(addr_a[1])] and (not register[exa.get(addr_b[0])][exa.get(addr_b[1])]))


def comp_n( n, a):
    addr_a = str(a)
    num = register[exa.get(addr_a[0])][exa.get(addr_a[1])]
    comp_res = cmp(n, num)

def comp_a( b, a):
    addr_a = str(a)
    addr_b = str(b)
    comp_res = cmp(register[exa.get(addr_a[0])][addr_a[1]], register[exa.get(addr_b[0])][exa.get(addr_b[1])])

def beq(label):
    if(comp_res == 0):
        next_i = labelled_i.get(label, "")

def bne(label):
    if(not comp_res == 0):
        next_i = labelled_i.get(label, "")

def bgt(label):
    if(comp_res > 0):
        next_i = labelled_i.get(label, "")

def blt(label):
    if(comp_res < 0):
        next_i = labelled_i.get(label, "")

def bge(label):
    if(comp_res >= 0):
        next_i = labelled_i.get(label, "")

def ble(label):
    if(comp_res <= 0):
        next_i = labelled_i.get(label, "")


#read
mem_size = raw_input().strip("\n")


operation = raw_input().strip("\n")
operation = operation.strip(" ")
operation = operation.split(" ")

while (not operation == "" or not next_i == ""):

    n = len(operation)
    new_operation = []
    for each in operation:
        if (not each == '' or each.isspace()):
            new_operation.append(each)
    if (len(new_operation) < 2):
        break
    operation = new_operation
    operator = operation[-2]
    operands = operation[-1].split(",")

    n = len(operation)
    #print operation

    if (n > 2):
        labl = operation[-3]

    if (operator == "PRINT"):
        if (len(operands) > 1):
            prt(operands[0], operands[1])
        else:
            prt(operands[0])
    elif (operator == "MOVE"):
        if(operands[0][0] == '#'):
            if(operands[1][0] == "("):
                move_n_da(operands[0][1:], operands[1])
            else:
                move_n_a(operands[0][1:], operands[1])
        else:
            if(operands[0][0] == "("):
                if(operands[1][0] == "("):
                    move_da_da(operands[0][1:-1], operands[1][1:-1])
                else:
                    move_da_a(operands[0][1:-1], operands[1])
            else:
                if(operands[1][0] == "("):
                    move_a_da(operands[0], operands[1][1:-1])
                else:
                    move_a_a(operands[0], operands[1])
    elif (operator == "ADD"):
        if(operands[0][0] == '#'):
            add_n(int(operands[0][1:]), operands[1])
        else:
            add_a(operands[0], operands[1])
    elif (operator == "SUB"):
        if(operands[0][0] == '#'):
            sub_n(int(operands[0][1:]), operands[1])
        else:
            sub_a(operands[0], operands[1])
    elif (operator == "AND"):
        if(operands[0][0] == '#'):
            and_n(int(operands[0][1:]), operands[1])
        else:
            and_a(operands[0], operands[1])
    elif (operator == "OR"):
        if(operands[0][0] == '#'):
            or_n(int(operands[0][1:]), operands[1])
        else:
            or_a(operands[0], operands[1])
    elif (operator == "XOR"):
        if(operands[0][0] == '#'):
            xor_n(int(operands[0][1:]), operands[1])
        else:
            xor_a(operands[0], operands[1])
    elif (operator == "COMP"):
        if(operands[0][0] == '#'):
            comp_n(int(operands[0][1:]), operands[1])
        else:
            comp_a(operands[0], operands[1])
    elif (operator == "BEQ"):
        beq(operands[0])

    elif (operator == "BNE"):
        bne(operands[0])
    elif (operator == "BGT"):
        bgt(operands[0])
    elif (operator == "BLT"):
        blt(operands[0])
    elif (operator == "BGE"):
        bge(operands[0])
    elif (operator == "BLE"):
        ble(operands[0])

    try:
        operation = raw_input().strip("\n")
        operation = operation.strip(" ")
        operation = operation.split(" ")
    except EOFError:
        break
