class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=list(set(nums))
        if len(x)<3:
            return max(x)
        else:
            x.sort()
            return x[-2]
