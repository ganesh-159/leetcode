class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=sorted(nums)
        s=set(n)
        l=list(s)
        fs=sorted(l)
        if len(fs)>=3:
            return fs[-3]
        else:
            return fs[-1]
        