class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0  # Minimum open brackets
        high = 0  # Maximum open brackets

        for i in s:
            if i == '(':
                low += 1
                high += 1
            elif i == ')':
                low = max(0, low - 1)  # Ensure it never goes below zero
                high -= 1
            elif i == '*':
                low = max(0, low - 1)  # '*' can be empty
                high += 1  # '*' can be '('
            
            if high < 0:  # Too many closing brackets
                return False
                
        return low == 0  # If there's a valid way to balance