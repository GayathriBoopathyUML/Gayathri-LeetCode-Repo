class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_=''
        for i in range(len(s)):
            new_ += s[indices.index(i)]
        return new_
        