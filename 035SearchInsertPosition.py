class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        k=0
        for i in nums:
            if target<=i:
                return k
            k+=1
        return k
            

class Solution(object):  #二分法，最快
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low,high=0,len(nums)-1
        while low<high:
            mid=(low+high)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid
        return low
            
