class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set()

        def backtrack(row,col,index):
            

            if index==len(word):
                return True

            if row < 0 or row >= len(board):
                return False
            if col < 0 or col >= len(board[0]):
                return False
            if board[row][col] != word[index]:
                return False
            if (row,col) in visited:
                return False

                #state mutation of spatial geometry
            visited.add((row,col))
                
                #recursion
            result = (backtrack(row+1,col,index+1) or
            backtrack(row-1,col,index+1) or
            backtrack(row,col+1,index+1) or
            backtrack(row,col-1,index+1))

                #reversion
            visited.remove((row,col))

            return result

        #find starting poiint
        for r in range(len(board)):
            for c in range(len(board[0])):

                if backtrack(r,c,0):
                    return True
        return False
        
