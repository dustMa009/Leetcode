'''
class Solution(object):   #太慢
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        res=''
        for each in s:
            if 96<ord(each)<123 or 47<ord(each)<58:
                res=res+each

        return res==res[::-1]
'''

class Solution(object):   #2.0
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res=''.join(list(filter(str.isalnum,s)))
        res=res.lower()
        return res==res[::-1]
