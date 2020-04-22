
class Solution:
    def twoSum(self, nums, target):
        cache = {}
        for index, num in enumerate(nums):
            if num in cache:
                return [cache[num], index]
            cache[target-num] = index

print(
    Solution().twoSum([3,3], 6)
)