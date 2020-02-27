class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=s
        while a[-1]==' ':
            a=a[:-1]
        return len(a)-1-a.rfind(' ')
