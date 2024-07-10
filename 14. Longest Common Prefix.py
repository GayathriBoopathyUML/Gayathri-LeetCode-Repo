class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        strs.sort()
        length = min(len(strs[0]), len(strs[size - 1]))
        i = 0
        while (i < length and 
            strs[0][i] == strs[size - 1][i]):
            i += 1
        word = strs[0][0: i]
        return word