class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations=[]
        nums.sort()

        def backtrack(index,subset):
            if len(subset)==len(nums):
                permutations.append(subset.copy())
                return

            
            for i in range(0,len(nums)):

                if nums[i] in subset:
                    continue
                
                subset.append(nums[i])

                backtrack(i+1,subset)

                subset.pop()

        backtrack(0,[])
        return permutations