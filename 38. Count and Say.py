class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)  # Get the previous sequence
        print(n,prev)
        res = ""
        count = 1

        for i in range(len(prev)):
            if i < len(prev) - 1 and prev[i] == prev[i + 1]:
                count += 1  # Count repeated characters
            else:
                res += str(count) + prev[i]  # Append count + digit
                count = 1  # Reset count
        print(res)
        return res
