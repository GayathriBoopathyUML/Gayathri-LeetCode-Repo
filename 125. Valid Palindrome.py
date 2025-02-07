class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (''.join(i.lower() for i in s if i.isalnum()))
        return s==s[::-1]
        

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1  # Skip non-alphanumeric characters
            while left < right and not s[right].isalnum():
                right -= 1  # Skip non-alphanumeric characters
            
            if s[left].lower() != s[right].lower():
                return False  # Characters do not match
            
            left += 1
            right -= 1
        
        return True  # The entire string is a palindrome
