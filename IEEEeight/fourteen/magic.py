__author__ = 'funso'


#read
n = int(raw_input())

mat = []
for j in range(n):
    r = raw_input().strip("\n")
    r = r.split(" ")
    new_r = []
    for each in r:
        if(each.isalnum()):
            new_r.append(int(each))
    mat.append(new_r)

#print mat

#sum main diagonal
diag_sum = 0
j = 0
for each in mat:
    diag_sum += each[j]
    j += 1

anti_sum = 0
s = n - 1
v = 0
while(s >= 0 and v <= n - 1):
    anti_sum += mat[v][s]
    s -= 1
    v += 1


col_sum = []
for m in range(n):
    suma = 0
    for q in range(n):
        suma += mat[q][m]
    col_sum.append(suma)

row_sum = []
for each in mat:
    row_sum.append(sum(each))

"""
print diag_sum
print anti_sum
print row_sum
print col_sum
"""

out = []
count = 0

j = -1
for each in col_sum:
    if not each == diag_sum:
        count += 1
        out.append(j)
    j -= 1

i = 0
for each in row_sum:
    if not each == diag_sum:
        count += 1
        out.append( i + 1)
    i += 1

if ( not diag_sum == anti_sum):
    count += 1
    out.append(0)
out.sort()
print count
for each in out:
    print each

