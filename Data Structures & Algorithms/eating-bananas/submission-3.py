class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        l=1
        r=max(piles)

        if n == h:
            return max(piles)

        
        while l <= r:
            k=(l+r)//2
            h_k=0

            for i in range(n):
                #round up division without ceil()
                h_k += int(-(-piles[i] // k))
            
            if h_k <= h:
                min_k=k
                r=k-1

            elif h_k > h:
                l=k+1
                
                
        
        return min_k






















        


