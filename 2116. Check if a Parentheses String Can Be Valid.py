# class Solution:
#     def canBeValid(self, s: str, locked: str) -> bool:
#         # print(s,locked)
#         change=0
#         if len(s)>1 and (s[0] != ')' or locked[0] !='1'):
#             for i,n in enumerate(locked):
#                 if n=='0':
#                     if change > 0: change -= 1
#                     if change < 0: change += 1
#                 elif n=='1':
#                     if s[i] == '(': change += 1
#                     if s[i] == ')': change -= 1
#                 # print(change)
#         elif s[0] == ')' and locked[0] =='1':
#             change -= 1
#         else:
#             if s == '(': change += 1
#             if s == ')': change -= 1
#         return (True if change==0 else False)
        

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False  # Odd length can't be balanced
        
        open_count = 0  # Open balance
        flexible = 0  # Tracks count of unlocked characters
        
        # Forward Pass (Left to Right) - Check `)`
        for i in range(len(s)):
            if locked[i] == '0':
                flexible += 1  # Can be '(' or ')'
            elif s[i] == '(':
                open_count += 1
            else:  # s[i] == ')'
                open_count -= 1
            
            if open_count + flexible < 0:
                return False  # Too many locked `)` at some point
        
        open_count = 0
        flexible = 0
        
        # Backward Pass (Right to Left) - Check `(`
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                flexible += 1  # Can be '(' or ')'
            elif s[i] == ')':
                open_count += 1
            else:  # s[i] == '('
                open_count -= 1
            
            if open_count + flexible < 0:
                return False  # Too many locked `(` at some point
        
        return True
