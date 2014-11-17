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
    dic = dict()
    for each in pan:
        dic[each] = dic.get(each, 0) + 1
    for j in range(len(''.join(pan))):
        rev = pan[-1::-1]
        r = rev.find(pan[j])

        if (not ((len(pan) - r - 1))  == j and dic[pan[j]] % 2 == 0 and dic[pan[j]] > 0):
            #n = pan.count(pan[j])
            dic[pan[j]] -= 2
            m = len(f_pan) / 2
            f_pan = f_pan[:m] + (pan[j] * 2) + f_pan[m:]



    if(f_pan[:] == f_pan[-1::-1]):
        pali.append(f_pan)
        res.append(len(f_pan) + 1)

print pali
print max(res)
