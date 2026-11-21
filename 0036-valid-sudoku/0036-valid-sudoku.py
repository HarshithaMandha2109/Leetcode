class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows=len(board)
        cols=len(board[0])
        for i in range(rows):
            seen=set()
            for j in range(cols):
                if board[i][j] in seen:
                    return False
                elif board[i][j]==".":
                    continue
                seen.add(board[i][j])
        for i in range(cols):
            seen=set()
            for j in range(cols):
                if board[j][i] in seen:
                    return False
                elif board[j][i]==".":
                    continue
                seen.add(board[j][i])
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen=set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l] in seen:
                           return False
                        elif board[k][l]==".":
                            continue

                        seen.add(board[k][l])
        return True
        