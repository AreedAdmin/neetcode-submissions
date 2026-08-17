class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations=[]


        def backtrack(index,subset):

            if sum(subset)==target:
                combinations.append(subset.copy())

            elif sum(subset) > target:

                return

            for i in range(index, len(nums)):

                subset.append(nums[i])


                backtrack(i, subset)

                subset.pop()

        backtrack(0,[])
        return combinations