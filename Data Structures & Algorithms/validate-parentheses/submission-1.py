class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        charactermap= {')':'(',
                        '}':'{',
                        ']':'['}

        for char in s:
            if char in charactermap:
                if stack and stack[-1] == charactermap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False


        