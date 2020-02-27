'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]

        res=[[1]]
        for i in range(1,numRows):
            t=[0]+res[i-1]+[0]
            we=[]
            for j in range(i+1):
                we.append(t[j]+t[j+1])
            res.append(we)

        return res
'''

class Solution(object):  #很简洁很快的方法
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        
        res=[[1]*(i+1) for i in range(numRows)]
        for i in range(1,numRows):
            for j in range(1,i):
                res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res
