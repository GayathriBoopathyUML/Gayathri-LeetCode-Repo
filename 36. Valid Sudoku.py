class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                boxI = (r//3)*3 + (c//3)
                if num in row[r] or num in col[c] or num in box[boxI]:
                    return False
                row[r].add(num)
                col[c].add(num)
                box[boxI].add(num)
        return True