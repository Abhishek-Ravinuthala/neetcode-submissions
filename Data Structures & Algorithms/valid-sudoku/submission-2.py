class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        boxMap = defaultdict(set)

        for i in range(9):
            for j in range(9):

                if board[i][j]=='.': continue

                if board[i][j] not in rowMap[i]:
                    rowMap[i].add(board[i][j])
                else:
                    return False
                
                if board[i][j] not in colMap[j]:
                    colMap[j].add(board[i][j])
                else:
                    return False
                
                if board[i][j] not in boxMap[tuple[i//3, j//3]]:
                    boxMap[tuple[i//3, j//3]].add(board[i][j])
                else:
                    return False
        return True
                


                
