import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-1*nums[i] for i in range(len(nums))]
        heapq.heapify(nums)

        while k > 0:
            val=heapq.heappop(nums)*-1
            k-=1

        return val