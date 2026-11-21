class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        if rows*cols!=r*c:
            return mat
        reshaped_matrix=[[0]*c for i in range(r)]
        for i in range(rows):
            for j in range(cols):
                index=i*cols+j
                new_row=index//c
                new_col=index%c
                reshaped_matrix[new_row][new_col]=mat[i][j]
        return reshaped_matrix

            



        