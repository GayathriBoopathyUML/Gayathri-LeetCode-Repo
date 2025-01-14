class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        val = False
        for i in range(len(s)):
            print(i, s[i:]+s[:i])
            if s[i:]+s[:i] == goal:
                val = True
        return val
        