class Solution:
    def oddString(self, words: List[str]) -> str:
        # result=[]
        # for i in words:
        #     result.append([ord(i[j])-ord(i[j-1]) for j in range(1,len(i))])
        # # print(result)
        # for i in range(len(result)):
        #     if result[i] in result[i+1:]:
        #         continue
        #     else:
        #         print(result[i],words[i])

        result = []
        for i in words:
            result.append([ord(i[j]) - ord(i[j - 1]) for j in range(1, len(i))])

        # Finding the unique difference pattern
        for i in range(len(result)):
            if result.count(result[i]) == 1:  # Ensuring the pattern appears exactly once
                return words[i]  # Return the corresponding word
        
        return ""  # Default return if no unique string is found
        