class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        permutations=[]

        def backtrack(open_count:int,closed_count:int,substring:str):
            #base case
            if len(substring)==2*n:
                permutations.append(substring)
                return

            #iteration

            #decision 1
            if open_count < n:
                backtrack(open_count+1,closed_count,substring + '(')

            if closed_count < open_count:
                backtrack(open_count,closed_count+1, substring+ ')')

        backtrack(0,0,'')

        return permutations
            
            
