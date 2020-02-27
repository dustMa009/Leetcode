'''
class Solution(object):  #太慢
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        t=len(nums)
        nums=list(set(nums))
        nums=[0]+nums+[t+1]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>1:
                j=nums[i-1]+1
                while j<nums[i]:
                    res.append(j)
                    j+=1
        return res
'''

class Solution(object):  #2.0，很快，O(n)级
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=list(range(1,len(nums)+1))
        for i in nums:
            res[i-1]=0
        j=0
        for i in res:
            if i!=0:
                res[j]=res[i]
                j+=1
        return res[0:j]

class Solution(object):  #其他简洁解法
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        s1=set(x for x in range(1,l+1))
        s2=set(nums)
        return list(s1-s2)
