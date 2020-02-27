class Solution(object):   #自己的解法
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a={}
        b={}
        c={}
        for i,x in enumerate(nums):
            if x not in a:
                a[x]=1
                b[x]=i
                c[x]=i
            else:
                a[x]+=1
                c[x]=i
        s=0
        for i in a:
            if a[i]>s:
                s=a[i]
        
        j=[]
        for i in a:
            if a[i]==s:
                j.append(c[i]+1-b[i])
                
        return min(j)

import collections
class Solution(object):   #最快的解法，思路是差不多的
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=collections.defaultdict(list)
        for i in range(len(nums)):
            a[nums[i]].append(i)

        s=0
        for i in a:
            s=max(s,len(a[i]))

        res=len(nums)
        for val in a.values():
            if s==len(val):
                res=min(res,val[-1]-val[0]+1)

        
        return res
