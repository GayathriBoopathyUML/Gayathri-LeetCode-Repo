class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 3:
            return 1
        
        s = ['1','2','2']
        i = 2
        while len(s) < n:
            next_num = '1' if s[-1] == '2' else '2'  # Alternate between 1 and 2.
            s.extend([next_num] * int(s[i]))  # Append the next number `s[index]` times.
            i += 1  # Move the pointer forward.
        return(s[:n].count('1'))
        