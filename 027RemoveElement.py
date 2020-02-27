class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        s=0
        for i in nums:
            if i == val:
                s+=1

        for j in range(s):
            nums.remove(val)
        self.nums=nums
        return len(nums)

'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        count = 0 
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
                
        return count

'''
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        for i in range(len(nums))[::-1]:
            if nums[i] == val:
                del nums[i]
'''
