# from typing import List
#
#
# def solve(nums, index, result, stepCounter):
#
#     if index >= len(nums):
#         return
#     # triplet.append(nums[index])
#     if stepCounter == 3:
#         return nums[index]
#
#     value = solve(nums, index+1, result, stepCounter)
#
#     # solve(nums, index + 1, result, [])
#     solve(nums, index + 1, result, triplet)
#     triplet.append(nums[index])
#     solve(nums, index + 1, result, triplet)
#
#
#
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) < 3:
#             return 0
#         result = []
#         solve(nums, 0, result, 1)
#         return result
#
#
# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))