__author__ = 'funso'


stack = list()


def match(st):
    stack = []
    start = "{[(<"
    end = "}])>"
    for s in st:
        print "Checking ", s
        if (s in start):
            stack.append(s)
            print stack
        else:
            if ( s in end):
                if (stack[-1] == start[end.find(s)]):
                    stack.pop()
                else:
                    stack.append(s)
                print stack
    if (len(stack) == 0):
        print "Matched"
    else:
        print "Mismatch"
