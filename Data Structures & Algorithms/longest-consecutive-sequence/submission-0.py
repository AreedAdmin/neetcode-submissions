class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        alist=sorted(set(nums))
        curr_streak=1
        max_streak = 1

        for i in range(len(alist)-1):

            if alist[i+1] - alist[i] == 1:

                curr_streak+=1
            else:
                max_streak = max(max_streak,curr_streak)
                curr_streak=1

        return max(max_streak,curr_streak)