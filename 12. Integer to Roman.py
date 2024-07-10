class Solution:
    def intToRoman(self, num: int) -> str:
        dic = dict({1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"})
        div = 1
        while num >= div:
            div *= 10
        div /= 10
        res = ""
        while num:
            lastNum = int(num / div)
            if lastNum <= 3:
                res += (dic[div] * lastNum)
            elif lastNum == 4:
                res += (dic[div] +
                            dic[div * 5])
            elif 5 <= lastNum <= 8:
                res += (dic[div * 5] +
                (dic[div] * (lastNum - 5)))
            elif lastNum == 9:
                res += (dic[div] +
                            dic[div * 10])
            num = math.floor(num % div)
            div /= 10
        return res