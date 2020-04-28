from typing import List


class Solution:
    def trap2(self, height: List[int]) -> int:
        leftMax = [0 for _ in height]
        rightMax = [0 for _ in height]
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i+1])
        result = 0
        print(leftMax)
        print(rightMax)
        # for i in range(len(height)):
        #     temp = min(leftMax[i], rightMax[i] - height[i])
        #     result += temp

        for i in range(len(height)-1, -1, -1):
            result += min(leftMax[i] - height[i], rightMax[i])
        return result

    def trap(self, height: List[int]) -> int:
        leftMax = rightMax = 0
        lCntr = 0
        rCntr = len(height) - 1
        result = 0
        while lCntr < rCntr:
            leftMax = max(leftMax, height[lCntr])
            rightMax = max((rightMax, height[rCntr]))
            if leftMax <= rightMax:
                result += leftMax - height[lCntr]
                lCntr += 1
            else:
                result += rightMax - height[rCntr]
                rCntr -= 1
        return result



print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([2,0,2]))