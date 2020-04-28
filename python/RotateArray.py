from typing import List

# https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if nums is None or len(nums) < 2 or k < 1:
            return
        k = k % len(nums)
        if k == 0:
            return
        def reverseSubstring(nums, start, end):
            while start < end:
                # temp = nums[start]
                # nums[start] = nums[end]
                # nums[end] = temp
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverseSubstring(nums, 0, len(nums) - k - 1)
        reverseSubstring(nums, len(nums) - k, len(nums) - 1)
        reverseSubstring(nums, 0, len(nums) - 1)

nums = [1,2,3,4,5,6]
Solution().rotate(nums, 3)
print(nums)