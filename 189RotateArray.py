'''
class Solution(object):   #有bug
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        res=[0]*len(nums)
        for i in range(len(nums)):
            t=(i+k)%len(nums)
            res[t]=nums[i]
        nums=res
        return nums
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        t=k%len(nums)
        res=nums[len(nums)-t:]
        nums[t:]=nums[0:len(nums)-t]
        nums[0:t]=res

'''
class Solution(object):  #简洁的表达
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[0: -k]
'''
