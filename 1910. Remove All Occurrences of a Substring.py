class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # k = s
        # while part in k:
        #     k = ''.join(k.split(part))
        # return(k)
        while part in s:
            s = s.replace(part, "", 1)  # Removes only the first occurrence in each iteration
        return s

        