class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #check rows
        for row in range(len(board)):
            seen=set()
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue

                if board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])

                
        #check cols
        for col in range(len(board[0])):
            seen=set()
            for row in range(len(board)):
                if board[row][col] == '.':
                    continue

                if board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])
        
        #check quadrants
        dictionary={}
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue

                quadrant=(row//3,col//3)

                if quadrant not in dictionary:

                    dictionary[quadrant]=set()
                    dictionary[quadrant].add(board[row][col])

                elif board[row][col] in dictionary[quadrant]:
                    return False

                else:
                    dictionary[quadrant].add(board[row][col])
        
        return True



