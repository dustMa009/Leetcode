class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        s=s[::-1]
        w=1
        
        for each in s:
            res+=(ord(each)-64)*w
            w=w*26
        return res
