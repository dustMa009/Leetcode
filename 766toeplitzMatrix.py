class Solution(object):    #比较慢
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix)==1 or len(matrix[0])==1:
            return True
        for i in range(1,len(matrix)):
            m=i
            n=0
            while m<len(matrix) and n<len(matrix[0]):
                if matrix[m][n]!=matrix[i][0]:
                    return False
                m+=1
                n+=1
        for i in range(len(matrix[0])):
            m=0
            n=i
            while m<len(matrix) and n<len(matrix[0]):
                if matrix[m][n]!=matrix[0][i]:
                    return False
                m+=1
                n+=1
        return True


class Solution(object):    #简洁的方法
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m=len(matrix)
        n=len(matrix[0])
        if m==1 or n==1:
            return True
        for i in range(0,m-1):
            for j in range(0,n-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True
