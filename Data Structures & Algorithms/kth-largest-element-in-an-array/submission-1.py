import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        kth LARGEST element therfore -> maxheap

        we heapify our maxheap then

        we run an iteration loop where we keep popping of the heap until we hit kth nuymber 

        return klth number
        '''
        maxheap=[-number for number in nums]

        heapq.heapify(maxheap)

        #while conditional to ekep popping for k

        while k > 0:
            value=heapq.heappop(maxheap)*-1
            k-=1
        return value
