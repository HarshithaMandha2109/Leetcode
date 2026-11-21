class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows=len(grid)
        cols=len(grid[0])
        arr=[]
        for i in range(rows):
            for j in range(cols):
                arr.append(grid[i][j])
        k=k%(rows*cols)
        arr=arr[-k:]+arr[:-k]
        ans=[]
        for i in range(rows):
            row=[]
            for j in range(cols):
                row.append(arr[i*cols+j])
            ans.append(row)
        return ans
        