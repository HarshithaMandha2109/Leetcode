class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        rows=len(matrix)
        cols=len(matrix[0])
        lucky=[]
        for i in range(cols):
            maxi=float("-inf")
            index=0
            for j in range(rows):
                if maxi<matrix[j][i]:
                    maxi=matrix[j][i]
                    index=j
            if maxi==min(matrix[index]):
                lucky.append (maxi)
        return lucky   

       