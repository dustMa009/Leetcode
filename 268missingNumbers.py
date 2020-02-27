class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t=len(nums)
        return t*(t+1)/2-sum(nums)
