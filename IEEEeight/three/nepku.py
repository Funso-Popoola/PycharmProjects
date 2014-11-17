___author__ = 'funso'

def produce_nepku(lst):
    i = 0
    nep = []
    while(i < len(lst)):

        item = lst[i]
        if ( item.isspace() or item == "."):
            continue
        count = 0
        while (i < len(lst) and lst[i] == item):
            count += 1
            i += 1
        nep = nep + [str(count), item]
    return nep

#read input
lst = raw_input().strip("\n")
lst = lst.split(" ")

k = int(lst[0])
lst.remove(lst[0])

lst[-1] = lst[-1].strip("\r")
res = [lst]
m = len(lst)
loop = 1
while loop <= k:
    lst = produce_nepku(lst)
    if len(lst) > m:
        m = len(lst)
    res.append(lst)
    loop += 1

maxi = len(res[-1])
for each in res:
    diff = m - len(''.join(each))
    print diff
    out = "." * diff
    if len(' '.join(each)) % 2 == 0:
        print "." + out + ' '.join(each) + out
    else:
        print out + ' '.join(each) + out

print maxi
