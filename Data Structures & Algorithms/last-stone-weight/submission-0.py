class Solution:
    def lastStoneWeight(self, maxheap: List[int]) -> int:
        maxheap=[-number for number in maxheap]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            x=-1*heapq.heappop(maxheap)
            y=-1*heapq.heappop(maxheap)

            if x==y:
                continue
            elif x < y:
                smashedy=(y-x)*-1
                heapq.heappush(maxheap, smashedy)
            elif x > y:
                smashedx=(x-y)*-1
                heapq.heappush(maxheap, smashedx)
        
        if len(maxheap) == 0:
            return 0
        else:
            return -1*maxheap[0]