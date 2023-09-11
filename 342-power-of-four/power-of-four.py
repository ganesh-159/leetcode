class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return 1
        else:
            if n//4 == n/4 and n>1:
                r=self.isPowerOfFour(n//4)
                return r
            else:
                return 0
