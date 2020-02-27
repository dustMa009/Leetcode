class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        for each in A:
            temp=each[::-1]
            for x in range(len(temp)):
                temp[x]=0 if temp[x] else 1
            res.append(temp)
        return res
