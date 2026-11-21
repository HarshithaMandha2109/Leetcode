class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=[]
        c=[]
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    if i not in r:
                        r.append(i)
                    if j not in c:
                        c.append(j)
        for i in range(rows):
            for j in range(cols):
                if i in r or j in c:
                    matrix[i][j]=0
        return matrix


        