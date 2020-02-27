class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res=''
        while n>0:
            t=n%26
            if t==0:
                t=26
            res=chr(t+64)+res
            if n>26:
                n=int(n/26)
            else:
                n=0

        return res
