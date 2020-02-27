'''
class Solution(object):   #AC了，很慢
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)==len(set(nums)):
            return False
        
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                a=nums.index(nums[i],i+1)
                if a-i<=k:
                    return True
        
        return False
'''

class Solution(object):   #最快的方法！击败98.6%的方法
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)==len(set(nums)):
            return False
        if k>=len(nums):
            return len(nums)!=len(set(nums))
        for i in range(len(nums)-k):
            if len(set(nums[i:i+k]))<k:
                return True

        return False

'''
class Solution(object):   #利用字典的优秀解法
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, v in enumerate(nums):
            if v in d and i - d[v] <= k:
                return True
            d[v] = i
        return False
