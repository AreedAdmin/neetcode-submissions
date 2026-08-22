class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_code=[0]*26
        t_code=[0]*26

        if len(s) != len(t):
            return False

        #populate s
        for i in range(len(s)):
            s_code[int(ord(s[i])-97)]+=1

            t_code[int(ord(t[i])-97)]+=1
        
        return s_code == t_code


