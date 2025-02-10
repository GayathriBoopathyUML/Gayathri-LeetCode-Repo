class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        r=num
        while l<=r:
            mid = (l+r)//2
            ms = mid*mid
            # print(l,r,mid,ms)
            if ms == num:
                return True
            elif ms < num:
                l = mid + 1
            else:
                r = mid - 1
        return False

        