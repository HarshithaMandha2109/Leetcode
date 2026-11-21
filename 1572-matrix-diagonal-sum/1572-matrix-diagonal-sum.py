class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        row=len(mat)
        col=len(mat[0])
        left_sum=0
        right_sum=0
        for i in range(row):
            for j in range(col):
                if i==j:
                    left_sum += mat[i][j]
                elif i+j == col-1 and i!=j :
                    right_sum += mat[i][j]
        return left_sum+right_sum  
        