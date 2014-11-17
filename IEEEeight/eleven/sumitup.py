__author__ = 'funso'


#read n
n = int(raw_input().strip("\n"))
#read arr
arr = (raw_input().strip("\n")).split(" ")
new_arr = []
for each in arr:
    if(each.isalnum()):
        new_arr.append(int(each))

arr = new_arr

#read q
q = int(raw_input().strip("\n"))


for i in range(q):
    x = int(raw_input().strip("\n"))
    suma = []
    for j in range(n):
        r = ((j - x) + n) % n
        suma.append(arr[j] + arr[r])
    arr = suma

print ( sum(arr) % (10**9 + 7))
