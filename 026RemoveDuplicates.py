class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = 0 
        for num in nums:
            if num != nums[count]:
                count += 1
                nums[count]=num
        return count+1

