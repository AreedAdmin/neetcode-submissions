class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        range_max=len(nums)

        for i in range(0,range_max+1):
            if i not in nums:
                return i