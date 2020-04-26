# https://leetcode.com/problems/reorganize-string/

# INCOMPLETE
class Solution:
    def reorganizeString(self, input: str) -> str:
        if len(input) < 2:
            return input
        if len(input) == 2:
            if input[0] == input [1]:
                return ""
            else:
                return  input


        charCounts = {}
        for char in input:
            count = charCounts.get(char)
            if count:
                charCounts[char] = count + 1
            else:
                charCounts[char] = 1

        maxAllowed = ((len(input)-1) // 2)+1
        for count in charCounts.values():
            if count > maxAllowed:
                return ""

        result = ""
        prevChar = ""
        for _ in range(len(input)):
            for char in charCounts.keys():
                if char == prevChar:
                    continue
                if charCounts[char] > 0:
                    result += char
                    count = charCounts[char]
                    charCounts[char] = count - 1
        return result

# print(Solution().reorganizeString("aab"))
print(Solution().reorganizeString("aaaaacbcb"))
