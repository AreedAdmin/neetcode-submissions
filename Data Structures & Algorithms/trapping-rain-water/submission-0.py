class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        we use a two pointer method here

        we need a global area and lcal area variables

        computing the area between two poles smaintains min(height_l,height_r)*r-l

        contingenent on no poles being in between whcih is is the case we must deduct the height
        of such poles from the computation

        volume taken becomes max ( min(height_l,height_r)-pole,0 )
        '''
        
        L,R=0,len(height)-1
        max_L,max_R=height[L],height[R]
        total_volume=0

        while L < R:

            if max_L < max_R:
                L+=1

                max_L=max(max_L,height[L])

                total_volume+= max_L-height[L]

            else:
                R-=1
                max_R=max(max_R,height[R])
                total_volume+= max_R-height[R]

        return total_volume







        