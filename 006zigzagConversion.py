'''
class Solution(object):  #不要用n方级的算法
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        subs=['']*numRows
        for i in range(numRows):
            for j in range(len(s)):
                if j%(2*numRows-2)==i or j%(2*numRows-2)==2*numRows-i-2:
                    subs[i]=subs[i]+s[j]

        result=''
        for i in range(numRows):
            result=result+subs[i]

        return result
'''

'''  
class Solution(object):  #2.0
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows >= len(s):
            return s
        subs=['']*numRows
        for i in range(len(s)):
            j=i%(2*numRows-2)
            if j<numRows:
                subs[j]=subs[j]+s[i]
            else:
                subs[2*numRows-2-j]=subs[2*numRows-2-j]+s[i]

        result=''
        for i in range(numRows):
            result=result+subs[i]

        return result

'''
class Solution(object):  #大神解法1，亮点是用index,step,计算第几行
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows >= len(s):
            return s
        L=['']*numRows
        index,step=0,1
        
        for x in s:
            L[index]+=x
            if index==numRows-1:
                step=-1
            elif index==0:
                step=1
            index+=step

        return ''.join(L)
