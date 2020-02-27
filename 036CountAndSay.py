class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        else:
            a=''  #当前字符
            b=0   #当前字符数量
            c=''  #结果字符串
            for i in Solution.countAndSay(self,n-1)+'0':
                if i!=a:
                    if b>0:
                        c=c+str(b)+a
                    a=i
                    b=1
                else:
                    b=b+1
                    
            return c
