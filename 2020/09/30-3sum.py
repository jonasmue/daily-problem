from collections import defaultdict


class Solution(object):
    def threeSum(self, nums):
        # Fill this in.
        missing2idx = defaultdict(list)
        triplets = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    continue
                missing = 0 - (nums[i] + nums[j])
                indices = [i, j]
                missing2idx[missing].append(indices)

        triplet_indices = set()
        for i, num in enumerate(nums):
            if not len(missing2idx[num]):
                continue
            for pair in missing2idx[num]:
                if i in pair:
                    continue

                idx1 = pair[0]
                idx2 = pair[1]
                if {idx1, idx2, i} in triplet_indices:
                    continue

                triplet_indices.add(frozenset({idx1, idx2, i}))
                triplets.append([nums[idx1], nums[idx2], num])

        return triplets


# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]
