__author__ = 'funso'


def find_max_crossing_sub_array(matrix, low, mid, high):
    left_sum = None
    max_left = None
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += matrix[i]
        if left_sum is None or sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = None
    sum = 0
    max_right = None
    for j in range(mid + 1, high + 1):
        sum += matrix[j]
        if right_sum is None or sum > right_sum:
            max_right = j
            right_sum = sum
    return max_left, max_right, left_sum + right_sum

def find_max_sub_array(matrix, low, high):
    if high == low:
        return low, high, matrix[low]
    else:
        mid = (low + high) / 2
        (left_low, left_high, left_sum) = find_max_sub_array(matrix, low, mid)
        (right_low, right_high, right_sum) = find_max_sub_array(matrix, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_sub_array(matrix,low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


li = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7 ]
print find_max_sub_array(li, 0, len(li) - 1)
