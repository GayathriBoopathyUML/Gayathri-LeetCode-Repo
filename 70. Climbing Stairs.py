class Solution:
    def climbStairs(self, n: int) -> int:
        result = {1:1,2:2}
        for i in range(1, n+1):
            if i in result.keys():
                continue
            result[i]=result[i-1]+result[i-2]
        return(result[n])
        