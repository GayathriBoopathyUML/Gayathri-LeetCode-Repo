class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1] * (i + 1) for i in range(numRows)]  # Initialize with 1s
        
        for i in range(2, numRows):  # Start from row 2 since first two rows are fixed
            for j in range(1, i):  # Avoid first and last element
                result[i][j] = result[i-1][j-1] + result[i-1][j]  # Sum of two above
        
        return result