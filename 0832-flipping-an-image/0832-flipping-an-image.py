class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        rows=len(image)
        cols=len(image[0])
        for i in range(rows):
            image[i]=image[i][::-1]
        for i in range(rows):
            for j in range(cols):
                if image[i][j]==0:
                    image[i][j]=1
                else:
                    image[i][j]=-0
        return image

        
        