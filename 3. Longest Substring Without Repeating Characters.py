class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        char_index_map = {}
        max_length = 0
        start = 0
        for end in range(n):
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                start = char_index_map[s[end]] + 1
            char_index_map[s[end]] = end
            max_length = max(max_length, end - start + 1)
        return max_length
