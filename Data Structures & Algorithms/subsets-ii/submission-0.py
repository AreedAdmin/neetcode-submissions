class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        combinations=[]
        nums.sort()
        def backtrack(index:int, subset:List):

                #base case
            if subset not in combinations:
                combinations.append(subset.copy())
            #iteration
            for i in range(index,len(nums)):

                #mutation (spatial geometry)

                subset.append(nums[i])

                #recursive dfs
                backtrack(i+1,subset)

                #reversion
                subset.pop()
        
        backtrack(0,[])

        return combinations

                

