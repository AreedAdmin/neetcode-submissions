class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        from heapq import nlargest
        counts=Counter(nums)
        return nlargest(k, counts, key=counts.get)