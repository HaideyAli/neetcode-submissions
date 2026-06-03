class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        theStack = []

        operators = {'+','-','*','/'}
        
        for t in tokens:
            if t not in operators:
                theStack.append(int(t))
                continue

            if t == '+':
                value = theStack[-2] + theStack[-1]
                for i in range(2):
                    theStack.pop()
                print(value)
                theStack.append(value)    
            elif t == '-':
                value = theStack[-2] - theStack[-1]
                for i in range(2):
                    theStack.pop()
                print(value)
                theStack.append(value) 
            elif t == '*':
                value = theStack[-2] * theStack[-1]
                for i in range(2):
                    theStack.pop()
                print(value)
                theStack.append(value) 
            else:
                # math.trunc is better in this case than // floor division
                # // will cause negative numbers to floor even lower
                value = math.trunc(theStack[-2] / theStack[-1])
                for i in range(2):
                    theStack.pop()
                print(value)
                theStack.append(value) 
        
        return theStack[0]