__author__ = 'funso'


t = raw_input().strip("\n")

l_i = 0
r_i = 0
lent = 1

res = []

pali = []
for i in range(len(t)):
    l_i = i
    rev = t[-1::-1]
    r_i = rev.find(t[i])

    pan = t[l_i:(len(t) - r_i)]
    print pan
    f_pan = ""

    new_pan = pan

    while(len(new_pan)  >= 1):
        print "/t/t", new_pan
        rev = new_pan[-1::-1]
        r = rev.find(new_pan[0])
        print "rrrrr=====", r
        item = new_pan[0]
        n = len(new_pan)
        print "NNNNNNN", n
        m = len(f_pan) / 2
        print f_pan, "Middle ---", m
        f = new_pan.find(new_pan[0])
        print "Found at ", f
        if ( n - r - 1 == f):
            print "here"
            new_pan = new_pan[f+1:]
        else:
            new_pan = new_pan[f+1:len(new_pan) - r - 1]
            print "Printing ===", f_pan
            f_pan = f_pan[:m] + (2 * item) + f_pan[m:]
            print "Printing ===", f_pan
    if(f_pan[:] == f_pan[-1::-1]):
        pali.append(f_pan)
        res.append(len(f_pan) + 1)
    print f_pan


    new_pan = pan

    while(len(new_pan)  >= 1):
        print "/t/t", new_pan
        rev = new_pan[-1::-1]
        r = rev.find(new_pan[0])
        print "rrrrr=====", r
        item = new_pan[0]
        n = len(new_pan)
        print "NNNNNNN", n
        m = len(f_pan) / 2
        print f_pan, "Middle ---", m
        f = new_pan.find(new_pan[0])
        print "Found at ", f
        if ( n - r - 1 == f):
            print "here"
            new_pan = new_pan[f+1:]
        else:
            new_pan = new_pan[f+1:len(new_pan) - r - 1]
            print "Printing ===", f_pan
            f_pan = f_pan[:m] + (2 * item) + f_pan[m:]
            print "Printing ===", f_pan
    if(f_pan[:] == f_pan[-1::-1]):
        pali.append(f_pan)
        res.append(len(f_pan) + 1)
    print f_pan

print "\t", pali
print max(res)
