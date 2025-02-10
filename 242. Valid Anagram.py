class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sc = sorted(s)
        # tc = sorted(t)
        sc = Counter(s)
        tc = Counter(t)
        return sc==tc
        