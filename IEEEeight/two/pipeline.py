__author__ = 'funso'


#read
n = int(raw_input())
arr = []
for i in range(int(n)):
    item = raw_input().strip("\n")
    item = item.strip("\r")
    item = item.split(" ")
    tem = list()
    tem += item[0:n]
    arr.append(tem)

print arr