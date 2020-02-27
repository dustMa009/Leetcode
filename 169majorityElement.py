'''
class Solution(object):  #太慢
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t=len(nums)
        while nums:
            i=nums[0]
            res=0
            while i in nums:
                res+=1
                nums.remove(i)

            if res>t/2:
                return i
'''

class Solution(object):  #2.0
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(nums)):
            if nums[i] not in l:
                s=0
                for ttt in nums[i:]:
                    if ttt==nums[i]:
                        s+=1
                if s>len(nums)/2:
                    return nums[i]
                else:
                    l.append(nums[i])


class Solution(object):  #直接的方法
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]
