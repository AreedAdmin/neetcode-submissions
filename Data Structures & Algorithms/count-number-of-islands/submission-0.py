class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        We use a localized counter to count the number of islands

        we iterate over every index in the 2d array via 2 for loops

        once we find a 1 (island) we add count +=1 then recursively perform dfs in every direction and 
        mutate the spatial geometry to 0 where the adjacent values are =1

        this essentially eliminates the island to all 0 such that they will not be double counted again.
        '''
        def dfs(row,col):
            # validate spatial boundary
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return

            # validate state
            if grid[row][col]=='0':
                return

            #origin state leakage
            grid[row][col]='0'

            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        

        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == '1':
                    count+=1

                    dfs(row,col)


        return count