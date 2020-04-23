class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stablePointer = 0
        movingPointer = 0
        maxLength = 0
        length = 0
        
        while movingPointer < len(s):
            if s[movingPointer] in s[stablePointer:movingPointer]:
                stablePointer += 1
                movingPointer = stablePointer
                maxLength = max(maxLength, length)
                length = 0
            length += 1
            movingPointer += 1
        return max(maxLength, length)

print(Solution().lengthOfLongestSubstring("dvdf"))