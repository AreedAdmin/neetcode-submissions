class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume=0
        #volume -> argmin(r_hright,l_height) * (r_index-l_index)
        #given this constraint the conditional for 
        #pointer movement depends on the bottleneck height

        l=0
        r=len(heights)-1

        while l < r:
            w=r-l
            h=min(heights[r],heights[l])

            volume=h*w

            if volume > max_volume:
                max_volume=volume


            if heights[r]<=heights[l]:
                r-=1
            else:
                l+=1

        return max_volume   
        
            





            