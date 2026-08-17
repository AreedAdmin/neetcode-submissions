class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations=[]
        running_total=0

        def backtrack(index:int,subset:List,running_total:int):

            if running_total==target:
                combinations.append(subset.copy())

            elif running_total > target:
                return

            for i in range(index, len(nums)):

                subset.append(nums[i])
                running_total+=nums[i]

                backtrack(i, subset,running_total)

                subset.pop()
                running_total-=nums[i]

        backtrack(0,[],running_total)
        return combinations