class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 1
        rs=1
        tep=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                tep+=1
            else:
                rs=max(rs,tep)
                tep=1
        return max(rs,tep)
