class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        minR = -(-len(b)//len(a))
        if b in a*minR:
            return minR
        if b in a*(minR+1):
            return minR+1
        return -1
        