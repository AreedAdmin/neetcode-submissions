class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products=[]
        for i in range(len(nums)):
            cum_prod=1
            for j in range(len(nums)):

                if j == i:
                    continue
                else:
                    cum_prod*=nums[j]

            products.append(cum_prod)

        return products


        