class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations=[]

        def backtrack(start:int, subset: List[int]):

            #base case , we hit end of the tree
            combinations.append(subset.copy())
        
        #iteration
            for i in range(start, len(nums)):

            #mutation, spatial progression fo the subset space 

                subset.append(nums[i])

            #recursion, recursively call abcktrack
                backtrack(i+1, subset)

                #reversion
                subset.pop()

        backtrack(0,[])

        return combinations

        