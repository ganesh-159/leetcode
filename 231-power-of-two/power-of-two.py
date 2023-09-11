class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return 1       
        else:
            if n//2 == n/2 and n>1:
                s=self.isPowerOfTwo(n//2)
                return s
            else:
                return 0
            