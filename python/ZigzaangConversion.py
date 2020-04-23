class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or len(s) == 1:
            return s

        result = ["" for _ in range(numRows)]
        lastRowIndex = numRows - 1
        goDown = True
        rowCounter = 0
        for char in s:
            result[rowCounter] = result[rowCounter] + char
            if rowCounter == 0:
                goDown = True
            if rowCounter == lastRowIndex:
                goDown = False
            if goDown:
                rowCounter += 1
            else:
                rowCounter -= 1
        return "".join(result)



print(Solution().convert("ABC", 1))