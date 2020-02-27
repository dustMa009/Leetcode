
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<=2:
            res=[]
            for each in nums:
                if each not in res:
                    res.append(each)
            return res
        else:
            nums.sort()
            res=[]
            a1=(len(nums)+1)//3-1
            a2=len(nums)-len(nums)//3-1
            if nums[a1]==nums[a2]:
                return [nums[a1]]
            else:
                if nums.count(nums[a1])>len(nums)//3:
                    res.append(nums[a1])
                if nums.count(nums[a2])>len(nums)//3:
                    res.append(nums[a2])
                return res


'''
class Solution(object):
    def majorityElement(self, nums):
        a,a_count = None,0
        b,b_count = None,0
        for num in nums:
            if num==a:
                a_count+=1
            elif num==b:
                b_count+=1
            elif a_count==0:
                a=num
                a_count=1
            elif b_count==0:
                b=num
                b_count=1
            else:
                a_count-=1
                b_count-=1
        ans=[]
        for elem in [a,b]:
            if nums.count(elem)>len(nums)/3:
                ans.append(elem)
        return ans
        
'''
