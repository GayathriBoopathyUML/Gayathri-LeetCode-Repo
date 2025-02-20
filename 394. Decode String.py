class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        result_s = ''
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            elif i == '[':
                stack.append((result_s,num))
                num = 0
                result_s = ''
            elif i == ']':
                last,n = stack.pop()
                result_s = last + n*result_s
            else:
                result_s += i
            # print(result_s,stack)   
        return result_s             