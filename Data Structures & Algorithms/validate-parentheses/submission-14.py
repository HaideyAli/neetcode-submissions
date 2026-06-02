class Solution:
    def isValid(self, s: str) -> bool:
        #We will put the last bracket type as the stack and pop once 
        bracketStack = []

        bracketSet = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        for c in s:
            if c in bracketSet.values():
                bracketStack.append(c)

            if c in bracketSet:
                if not bracketStack or bracketSet.get(c) != bracketStack[-1]:
                    return False
                else:
                    bracketStack.pop()

        if len(bracketStack) != 0:
            return False

        return True