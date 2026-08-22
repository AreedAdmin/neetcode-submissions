class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_code=[0]*26


        if len(s) != len(t):
            return False

        #populate s
        for i in range(len(s)):
            s_code[int(ord(s[i])-97)]+=1

            s_code[int(ord(t[i])-97)]-=1
        
        for val in s_code:
            if val != 0:
                return False
        return True


