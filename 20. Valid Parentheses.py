class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        openPara = ["[","(","{"]
        closePara = ["]",")","}"]
        for i in s:
            if i in openPara:
                stack.append(i)
            elif i in closePara:
                pos = closePara.index(i)
                if ((len(stack) > 0) and
                    (openPara[pos] == stack[len(stack)-1])):
                    stack.pop() 
                else: return False

        return len(stack) == 0
        