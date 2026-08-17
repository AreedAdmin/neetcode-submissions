class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack=[]

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped=stack.pop()

                result[popped]=i-popped

            stack.append(i)

        return result