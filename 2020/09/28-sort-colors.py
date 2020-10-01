from collections import Counter


class Solution:
    def sortColors(self, nums):
        l, r, red_pointer = 0, len(nums) - 1, 0
        while l <= r:
            if nums[l] == 0:
                nums[l], nums[red_pointer] = nums[red_pointer], nums[l]
                l += 1
                red_pointer += 1
            elif nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1


nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
