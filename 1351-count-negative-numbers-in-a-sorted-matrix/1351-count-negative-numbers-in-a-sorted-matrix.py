class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        negative_count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if  grid[i][j]<0:
                    negative_count+=1
        return negative_count        