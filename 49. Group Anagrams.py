class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            k = ''.join(sorted(i))
            if k in dic:
                dic[k].append(i)
            else:
                dic[k] = [i]
        return list(dic.values())
                