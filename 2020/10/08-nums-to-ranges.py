def findRanges(nums):
    result = []
    if not len(nums):
        return result
    separator = "->"
    current_range_start = nums[0]

    for i in range(1, len(nums)):
        prev_num = nums[i - 1]
        current_num = nums[i]
        if current_num - prev_num > 1:
            result.append(str(current_range_start) + separator + str(prev_num))
            current_range_start = current_num

    result.append(str(current_range_start) + separator + str(nums[-1]))
    return result


print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']
