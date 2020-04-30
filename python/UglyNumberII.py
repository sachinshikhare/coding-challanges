import math

class Solution:

    def nthUglyNumber(self, n: int) -> int:

        if n < 6:
            return n

        dp = [1]
        count = 0
        twoCounter = threeCounter = fiveCounter = 0
        while count < n:
            temp2 = 2 * dp[twoCounter]
            temp3 = 3 * dp[threeCounter]
            temp5 = 5 * dp[fiveCounter]
            temp = min(temp2, temp3, temp5)
            
            if temp == temp2:
                twoCounter += 1
            if temp == temp3:
                threeCounter += 1
            if temp == temp5:
                fiveCounter += 1

            dp.append(temp)
            count += 1
        return dp[n-1]

print(Solution().nthUglyNumber(10))
