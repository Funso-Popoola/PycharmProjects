__author__ = 'funso'


#read  s e p n
raw = raw_input().strip("\n")
raw = raw.split(" ")
new_raw = []
for each in raw:
    if(each.isalnum()):
        new_raw.append(each)
raw = new_raw
s = int(raw[0])
e = int(raw[1])
p = int(raw[2])  # winning index
n = int(raw[3])

user = []
for i in range(n):
    r = (raw_input().strip("\n"))
    user.append(r.strip(" "))
#mm = min(user)
lot_seq = []
for num in range(s, e+1):
    for each in user:
        if(each in str(num)):
            lot_seq.append(num)
            break

if( p - 1 < len(lot_seq)):
    print lot_seq[p - 1]
else:
    print "DOES NOT EXIST"
