class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row,col):
            #validate spatial geometry
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return 0

            #validate state
            if grid[row][col]==0:
                return 0

            #apply mutation
            grid[row][col]=0
            
            #apply recursive traversal & count accumulation
            return(1 + 
            dfs(row+1,col)+
            dfs(row-1,col)+
            dfs(row,col+1)+
            dfs(row,col-1)
            )

        max_count=0

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col]==1:
                    current_area=dfs(row,col)
                    if current_area > max_count:
                        max_count=current_area


        return max_count