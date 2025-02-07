class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strlist = s.rstrip().split(' ')
        return (len(strlist[-1]))
        