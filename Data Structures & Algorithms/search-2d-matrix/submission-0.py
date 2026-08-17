class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first check last element of each row to find if the last vlaue is greater or equal to target
        #then we use the pointers method by starting with l at 0 index of row i and r as last index of row i
        #if while loop ends without giving back the correct value that means that the value is not found in target
        m=len(matrix[0]) - 1
        target_row=None
        left=0
        right=len(matrix) - 1
        

        #binary serach for the correct row first then binary search again for the coorect index
        while left <= right:
            mid=(left+right)//2

            if matrix[mid][m] < target:
                left = mid + 1

            elif matrix[mid][0] > target:
                right = mid - 1

            elif matrix[mid][m] >= target and matrix[mid][0] <= target:
                #correct row
                target_row=mid
                break
        
        if target_row is None:
            return False

        left=0
        right=len(matrix[0]) - 1

        while left <= right:
            mid=(left+right)//2

            if matrix[target_row][mid] < target:
                left=mid+1
            elif matrix[target_row][mid] > target:
                right=mid-1
            
            elif matrix[target_row][mid] == target:
                return True
        
        return False

        




