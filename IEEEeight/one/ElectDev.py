__author__ = 'funso'

def quick_sort(lst, i, j):

    def find_pivot(aList, i, j):
        return (i + j) / 2

    def swap(lst, i, j):
        temp = lst[j]
        lst[j] = lst[i]
        lst[i] = temp

    def partition(aList, l, r, pivot):
        time = 1
        while(l < r or time == 1):
            l += 1
            while(aList[l] < pivot):
                l += 1

            while(not r == 0):
                r -= 1
                if aList[r] < pivot:
                    break
            swap(aList, l, r)
            time += 1
        swap(aList, l, r)
        return l

    pivot_i = find_pivot(lst, i, j)

    swap(lst, pivot_i, j)
    k = partition(lst, i - 1, j, lst[j])
    swap(lst, k, j)
    if (k - i) > 1:
        quick_sort(lst, i, k - 1)
    if (j - k) > 1:
        quick_sort(lst, k + 1, j)



def find_k(li):
    quick_sort(li, 0, len(li) - 1)
    return li[k - 1]

#read n
val = raw_input().split(" ")
new_val = []
for each in val:
    if each.isalnum():
        new_val.append(int(each))

n = int(new_val[0])
m = int(new_val[1])
k = int(new_val[2])

num = (raw_input().strip("\n")).strip("\r")
num = num.split(" ")
num[-1] = num[-1].strip("\r")
new_num = []
for ki in range(len(num)):
    if num[ki] == '' or num[ki].isspace():
        continue
    new_num.append(int(num[ki]))

num = new_num
sub = list()
start = 0
end = m
ks = []
for i in range(n):
    if ( start > end ):
        sub.append(num[start:] + num[:end + 1])
    else:
        sub.append(num[start:end ])
    ks.append(find_k(sub[i]))
    start = (start + 1) % n
    end = (end + 1) % (n + 1)

print min(ks)