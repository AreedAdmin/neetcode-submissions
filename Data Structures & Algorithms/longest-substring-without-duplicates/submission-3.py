class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #left pointer start of any substring
        #right pointer next char of any substring
        # left = right when we find a duplicate
        #use set for O(1) lookup
        max_count=0
        left=0
        right=0
        seen=set()
        count=0

        if len(s) == 1:
            return 1    

        while right < len(s):

            while s[right] in seen: #found duplicate
                seen.remove(s[left])
                left+=1
                count-=1
            
            else:
                seen.add(s[right])
                count+=1
                right+=1

                if count > max_count:
                    max_count=count

        return max_count

        

            






