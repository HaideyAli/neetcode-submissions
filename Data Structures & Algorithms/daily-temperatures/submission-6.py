class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #pair: temp, index

        for i, t in enumerate(temperatures):
            #while stack isn't empty an current temp > top of stack
            while stack and t > stack[-1][0]:
                stackInd = stack.pop()[1]
                result[stackInd] = (i - stackInd)
            
            stack.append((t,i))
        return result