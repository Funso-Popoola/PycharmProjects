__author__ = 'funso'


dico = dict()
#read
raw = raw_input().strip("\n")
raw = raw.strip("\r")
raw = raw.split(" ")
n = int(raw[0])
m = int(raw[1])

for i in range(m):
    inp = (raw_input().strip("\n")).strip("\r")
    inp = inp.split(" ")
    dico[inp[1]] = dico.get(inp[1], []) + [inp[0]]

subj = raw_input().strip("\n")
subj = subj.strip("\r")
subj = subj.split(" ")

print subj
print dico

out = "YES"
for i in range(len(subj)):
    pre = dico.get(subj[i], [])
    for each in pre:
        if( not each in subj[:i]):
            out =  "NO"
            break
print out