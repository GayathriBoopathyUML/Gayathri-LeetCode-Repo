class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Q={}
        # color={}
        # count=[]
        # for i in queries:
        #     if i[0] in Q:
        #         Q[i[0]] +=1
        #     else:
        #         Q[i[0]] = 1
        #     if i[1] in color:
        #         color[i[1]] +=1
        #     else:
        #         color[i[1]] = 1
        #     count.append(min(len(color),len(Q)))
        #     print(color,Q)
        # return(count)
        
        ans = []
        ballToColor = {}
        colorCount = collections.Counter()

        for ball, color in queries:
            if ball in ballToColor:
                prevColor = ballToColor[ball]
                colorCount[prevColor] -= 1
                if colorCount[prevColor] == 0:
                    del colorCount[prevColor]
            ballToColor[ball] = color
            colorCount[color] += 1
            ans.append(len(colorCount))

        return ans