class Solution:
    def reverse(self, x: int) -> int:
        num = x
        rev=0
        if(num<0):
            x = abs(x)
            while(x>0):
                dig=x%10
                rev=rev*10+dig
                x=x//10
            if rev < -2**31 or rev > 2**31 - 1:
                return 0
            else:
                return -abs(rev)
        else:
            while(x>0):
                dig=x%10
                rev=rev*10+dig
                x=x//10
            if rev < -2**31 or rev > 2**31 - 1:
                return 0
            else:
                return rev

        
        