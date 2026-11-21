class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        n=len(matrix)
        m=len(matrix[0])
        tp=[[0]*n for i in range(m)]
        for i in range(n):
            for j in range(m):
                tp[j][i]=matrix[i][j]
        return tp

        