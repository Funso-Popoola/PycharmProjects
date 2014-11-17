__author__ = 'funso'


class Sorter():

    def __init__(self, list):
        self.list = list

    def bubble_sort(self):
        # notoriously slow!
        #invariant: data item to the right are sorted
        for i in range(len(self.list)):
            j = 0
            while j < (len(self.list) - (i + 1)):
                if self.list[j] > self.list[j + 1]:
                    temp = self.list[j];
                    self.list[j] = self.list[j + 1]
                    self.list[j + 1] = temp
                j += 1

    def selection_sort(self):
        for i in range(len(self.list)):
            least_v = self.list[i]
            least_i = i
            for j in range(i+1, len(self.list)):
                if least_v > self.list[j]:
                    least_i = j
                    least_v = self.list[j]
            if not least_i == i:
                self.list[least_i], self.list[i] = self.list[i], self.list[least_i]

    def insertion_sort(self):
        for j in range(1, len(self.list)):
            key = self.list[j]
            i = j - 1
            while ( i >= 0 and self.list[i] > key ):
                self.list[i + 1] = self.list[i]
                i = i - 1
            self.list[i + 1] = key

    def merge_sort(self):

        def divide(aList, start, end):
            if(end > start):
                middle = (start + end) / 2
                divide(aList, start, middle)
                divide(aList, middle + 1, end)
                conquer(aList, start, middle, end)

        def conquer(aList, start, middle, end):
            temp = list()
            k = 0
            left_i = start
            right_i = middle + 1

            while( left_i <= middle and right_i <= end):
                if( aList[left_i] < aList[right_i] ):
                    temp.append(aList[left_i])
                    left_i += 1
                    k += 1
                else:
                    temp.append(aList[right_i])
                    right_i += 1
                    k += 1

            while( left_i <= middle ):
                temp.append(aList[left_i])
                left_i += 1
                k += 1

            while(right_i <= end ):
                temp.append(aList[right_i])
                right_i += 1
                k += 1

            for i in range(start, end + 1):
                aList[i] = temp[i - start]

        divide(self.list, 0, len(self.list) - 1)

    def quick_sort(self, i, j):

        def find_pivot(aList, i, j):
            return (i + j) / 2

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
                self.swap(l, r)
                time += 1
            self.swap(l, r)
            return l

        pivot_i = find_pivot(self.list, i, j)

        self.swap(pivot_i, j)
        k = partition(self.list, i - 1, j, self.list[j])
        self.swap(k, j)
        if (k - i) > 1:
            self.quick_sort(i, k - 1)
        if (j - k) > 1:
            self.quick_sort(k + 1, j)

    def swap(self, i, j):
        temp = self.list[j]
        self.list[j] = self.list[i]
        self.list[i] = temp

    def heap_sort(self):
        heap_size = len(self.list) - 1
        def parent(i):
            return i / 2

        def left(i):
            return 2 * i

        def right(i):
            return 2 * i + 1

        def max_heapify(arr, i):
            l = left(i)
            r = right(i)
            if l <= heap_size and arr[l] > arr[i]:
                largest = l
            else:
                largest = i
            if r <= heap_size and arr[r] > arr[largest]:
                largest = r
            if not largest == i:
                arr[i] , arr[largest] = arr[largest], arr[i]
                max_heapify(arr, largest)

        def build_max_heap(arr):
            global heap_size
            heap_size = len(arr) - 1
            for i in range(((len(arr) - 1) / 2), -1, -1):
                max_heapify(arr, i)

        build_max_heap(self.list)
        for i in range(len(self.list) - 1, 0, -1):
            self.list[0], self.list[i] = self.list[i], self.list[0]
            heap_size -= 1
            max_heapify(self.list, 0)





myList = [13, 2, 2, 1, 5]
sorter = Sorter(myList)
sorter.quick_sort(0, 4)
print sorter.list