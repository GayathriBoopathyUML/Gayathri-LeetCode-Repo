class Solution:
    def makeGood(self, s: str) -> str:
        newS = []  # Use a list to build the string efficiently
        for char in s:
            if newS and abs(ord(newS[-1]) - ord(char)) == 32:
                newS.pop()  # Remove bad adjacent pair
            else:
                newS.append(char)  # Keep valid characters
        return "".join(newS)  # Convert list back to string
        