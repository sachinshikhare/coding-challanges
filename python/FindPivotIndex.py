from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        cache = []
        subTotal = 0
        for num in nums:
            subTotal += num
            cache.append(subTotal)

        if len(cache) > 0:
            if cache[-1] - cache[0] == 0:
                return 0
        for index, value in enumerate(nums):
            if index == 0:
                continue
            if cache[index-1] == cache[-1] - cache[index]:
                return index

        if len(cache) > 0:
            if cache[-2] == 0:
                return len(nums)-1

        return -1

print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
print(Solution().pivotIndex([-1,-1,-1,0,1,1]))
print(Solution().pivotIndex([]))
print(Solution().pivotIndex([-1,-1,0,1,1,0]))
print(Solution().pivotIndex([-1,-1,1,1,0,0]))

print(Solution().pivotIndex([-1,-1,0,1,1,-1]))

print(Solution().pivotIndex([0,-1,-1,-1,-1,-1]))
