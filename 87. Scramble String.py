from functools import lru_cache
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def diff(x,y):
            # print(x,y)
            if x == y:
                return True
            if sorted(x) != sorted(y):
                return False
            for i in range(1,len(x)):
                # Case 1: No swapping
                if diff(x[:i], y[:i]) and diff(x[i:], y[i:]):
                    return True
                # Case 2: Swapping
                if diff(x[:i], y[-i:]) and diff(x[i:], y[:-i]):
                    return True
            return False
        return(diff(s1,s2))