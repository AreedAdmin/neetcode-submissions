class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        dentify sorted partition 

        check if the target falls within boundary of this sorted partition

        readjust spatial geometry

        repeat the process while left < right

        the ifdea is to also continue partition the data vbia our 3 pointers and determining the sorted partition
        becuase we are guaranteed to ahve atleast one sorted partition at any given time
        '''
        L=0
        R=len(nums)-1

        while L <= R:
            mid=(L+R)//2
            
            if nums[mid] == target:
                return mid

            #identify sorted partition
            if nums[L] <= nums[mid]: #left partition sorted

                if nums[L] <= target and target <= nums[mid]:
                    R=mid
                else:
                    L=mid+1
            
            else: #right partition sorted

                if nums[mid] <= target and target <= nums[R]:
                    L=mid
                else:
                    R=mid-1

        return -1
            

        