# class Solution:
#     def areAlmostEqual(self, s1: str, s2: str) -> bool:
#         str2=list(s2)
#         if s1 == s2:
#             return True
#         for i in range(len(str2)//2):
#             str2[i],str2[-i-1] = str2[-i-1],str2[i]
#             a = ''.join(str2)
#             if a == s1:
#                 return True
#             str2=list(s2)
#         return False
        
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        # Find indices where s1 and s2 differ
        diff = [(i, s1[i], s2[i]) for i in range(len(s1)) if s1[i] != s2[i]]
        print(diff)
        
        # There should be exactly two differences, and swapping them should make s1 == s2
        return len(diff) == 2 and diff[0][1] == diff[1][2] and diff[0][2] == diff[1][1]
