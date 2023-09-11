class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return 1
        else:
            if n//3 == n/3 and n>1:
                r=self.isPowerOfThree(n//3)
                return r
            else:
                return 0

        