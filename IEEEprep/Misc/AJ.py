__author__ = 'funso'


#read input
n = int(raw_input().strip("\n"))  # the number of sub-hills
slopes = raw_input().strip("\n")
slopes = slopes.split(" ")
print slopes

i = 0
while i < len(slopes):
    if slopes[i] == '' or slopes[i] == ' ':
        slopes.remove(slopes[i])
    else:
        i += 1

print slopes

assert (len(slopes) == n)

for i in range(n):
    slopes[i] = int(slopes[i])

sumList = list()
total = sum(slopes)
for i in range(n):
    sumList.append(total - sum(slopes[0:(i + 1)]))

print sumList
print(max(sumList))

