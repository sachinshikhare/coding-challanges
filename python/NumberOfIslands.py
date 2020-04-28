from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        maxRows = len(grid)
        maxCols = len(grid[0])
        if maxRows == 1 and maxCols == 1:
            return 1 if grid[0][0] == 1 else 0
        elif maxRows == 2 and maxCols == 2:
            atleastOne = any(any(val == 1 for val in row) for row in grid)
            return 1 if atleastOne else 0
        visited = [[cell==0 for cell in row] for row in grid]

        def visitNeghbours(grid, rowCounter, colCounter, visited):
            if rowCounter < 0 or rowCounter >= maxRows or colCounter < 0 or colCounter >= maxCols:
                return
            if visited[rowCounter][colCounter]:
                return
            else:
                visited[rowCounter][colCounter] = True
            visitNeghbours(grid, rowCounter, colCounter + 1, visited)
            visitNeghbours(grid, rowCounter, colCounter - 1, visited)

            visitNeghbours(grid, rowCounter + 1, colCounter, visited)
            visitNeghbours(grid, rowCounter - 1, colCounter, visited)
            return

        islandCount = 0
        for rowCounter in range(len(grid)):
            for colCounter in range(len(grid[0])):
                if not visited[rowCounter][colCounter]:
                    islandCount += 1
                    visitNeghbours(grid, rowCounter, colCounter, visited)
        return islandCount

grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]

print(Solution().numIslands(grid))

grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]

print(Solution().numIslands(grid))