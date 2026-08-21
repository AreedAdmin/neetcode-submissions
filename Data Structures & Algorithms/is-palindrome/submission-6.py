class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        we want to find if s is palindrome meaning is s == s[::-1]
        
        When we find a grammar character we just skip it 

        we have converging pointers on either side of the stirng and chcek each
        character at L and R indices
        '''
        L=0
        R=len(s)-1

        while L <= R: #traversal conditional

            # if conditionals for grammar
            if s[L] in " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
                L+=1
                continue
                
            elif s[R] in " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
                R-=1
                continue
            
            # if conditional logic for checking palindromic property

            sl=s[L].lower()
            sr=s[R].lower()

            if sl==sr:
                L+=1
                R-=1
            else:
                return False
        
        return True
