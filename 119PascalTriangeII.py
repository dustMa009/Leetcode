class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]

        res=[1]*(rowIndex+1)
        for  i in range(1,rowIndex+1):
            res[i]=int((rowIndex+1-i)*res[i-1]/i)

        return res
