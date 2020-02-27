'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sums=0
        start,end=0,nums[0]
        for i in nums:
            sums=sums+i
            if sums>end:
                end=sums
            if sums<start:
                t=end-start
                start=sums
                end=start+t
    
        return end-start
'''

class Solution(object):   #大神解答，我都不明白怎么想出来的，感觉好不自然
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i=0
        l=len(nums)
        sums=0
        maxsum=nums[0]
        while i<l:
            if sums<0:
                sums=nums[i]
            else:
                sums+=nums[i]
            i++

            if sums>maxsum:
                maxsum=sums
        return maxsum
    

