from typing import List


def solve(nums, index, result, triplet):

    if index >= len(nums):
        return
    # triplet.append(nums[index])
    if len(triplet) == 3:
        if sum(triplet) == 0:
            print(triplet, sum(triplet))
            result.append(triplet)
            return
        else:
            solve(nums, index+1, result, triplet.remove(triplet[0]))

    # solve(nums, index + 1, result, [])
    solve(nums, index + 1, result, triplet)
    triplet.append(nums[index])
    solve(nums, index + 1, result, triplet)



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return 0
        result = []
        solve(nums, 0, result, [])
        return result


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))