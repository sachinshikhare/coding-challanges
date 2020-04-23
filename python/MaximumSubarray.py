from typing import List
import sys


class Solution:

    def maxSubArray3(self, nums: List[int]) -> int:
        return_max = nums[0]
        current_max = nums[0]

        for i in range(1, len(nums)):
            print(current_max, return_max)
            current_max = max(nums[i], nums[i] + current_max)
            return_max = max(return_max, current_max)

        return return_max


    def maxSubArray2(self, nums: List[int]) -> int:
        print(nums)
        currMax = nums[0]
        retMax = nums[0]
        for num in nums[1:]:
            print(currMax, retMax)
            currMax = max(num, currMax + num)
            retMax = max(retMax, currMax)
        return retMax

    def maxSubArray(self, nums: List[int]) -> int:
        if nums and len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        mid = len(nums)//2
        lsum = self.maxSubArray(nums[:mid])
        rsum = self.maxSubArray(nums[mid:])
        ccsum = self.maxCrossSubArray(nums, mid)
        print("ccsum", ccsum)
        return max(lsum, rsum, ccsum)


    def maxCrossSubArray(self, nums, mid):
        if len(nums) == 2:
            return max(nums[0], nums[1], nums[0] + nums[1])
        max_l_sum = max_r_sum = float('-inf')
        sum = 0
        for index in range(mid-1, -1, -1):
            sum += nums[index]
            max_l_sum = max(max_l_sum, sum)

        sum = 0

        for i in range(mid,len(nums),1):
            sum += nums[i]
            max_r_sum = max( max_r_sum ,sum)
        return max_l_sum + max_r_sum



# print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))
print()
# print(Solution().maxSubArray3([-2,1,-3,4,-1,2,1,-5,4]))