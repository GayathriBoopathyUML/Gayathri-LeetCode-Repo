class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s += str(i)
        num = int(s)+1
        returnList =[]
        for i in str(num):
            returnList.append(int(i))
        return(returnList)
    


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # Process from the last digit to the first
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # Return early since there's no carry forward
            digits[i] = 0  # Set to 0 and continue loop for carry

        # If we exit the loop, it means all digits were 9 (e.g., 999 → 1000)
        return [1] + digits
