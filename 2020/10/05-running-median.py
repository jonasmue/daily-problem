def find_insertion_point(array, key):
    if not len(array):
        return 0
    if key > array[-1]:
        return len(array)
    if key < array[0]:
        return 0
    lower, upper, middle = 0, len(array), len(array) // 2
    while lower < upper:
        mid_value = array[middle]
        if mid_value == key:
            return middle
        if mid_value > key:
            upper = middle
        else:
            lower = middle + 1
        middle = (upper + lower) // 2
    return middle


def running_median(stream):
    running_median = []
    running_sorted_list = []
    for index, value in enumerate(stream):
        current_length = index + 1
        insertion_index = find_insertion_point(running_sorted_list, value)
        running_sorted_list.insert(insertion_index, value)
        if current_length % 2:
            # Odd length
            median = running_sorted_list[current_length // 2]
        else:
            # Even length
            median = (running_sorted_list[current_length // 2 - 1] + running_sorted_list[current_length // 2]) / 2
        running_median.append(median)
    return running_median


print(running_median([2, 1, 4, 7, 2, 0, 5]))
# 2 1.5 2 3.0 2 2.0 2
