class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        The condition ni + nj + nk = 0:
            must be satisfied which we can rearrange to:

        nj + nk = -ni
        therefore we can iterate i over the segment of the list that is 
        negatives or 0

        to do this we must sort the list

        then for the j and k indices we create a double loop that traverses
        the remaining spatial geometry wehre we satisfy

        i != j != k therefore we maintain i < j < k over the course of our algorithm

        rather than a double loop given our array is sroted we can then deploy a two pointer approach
        for traversign, J and K to reduce this to O(N*N)

        we need to deploy converging pointers such that we have clear conditional definitions on how to traverse our pointers
        '''
        #Create  iterator
        i=0
        #sort the list
        nums.sort()
        results=[]

        #Iterate i while i is a negative number or 0
        while  i < len(nums):
            target = -1*nums[i]

            J=i+1
            K=len(nums)-1
            
            while J < K:
                if nums[J] + nums[K] == target:
                    if [nums[i],nums[J],nums[K]] not in results:
                        results.append([nums[i],nums[J],nums[K]])
                    J+=1
                elif nums[J]+nums[K] < target:
                    J+=1
                else:
                    K-=1
            
            i+=1
        
        return results

                




            