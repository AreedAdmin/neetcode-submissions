class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        We use sliding window pattern here
        loop through and check at every spatial geometry advancement if our sum has gone to below 0
        if so we reset back to 0 and iterate
        we consistently add to our list that starts with nums[0]
        '''
        max_sum=nums[0]
        curr_sum=0


        for R in range(len(nums)):
            curr_sum=max(curr_sum,0)
            curr_sum+=nums[R]

            if curr_sum > max_sum:
                max_sum=curr_sum
        return max_sum

