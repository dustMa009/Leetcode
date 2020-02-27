'''class Solution(object):   #太慢，2的n-1次方
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s==s[::-1]:
            return s
        else:
            a=Solution.longestPalindrome(self,s[1:])
            b=Solution.longestPalindrome(self,s[:-1])
            if len(b)>=len(a):
                return b
            else:
                return a
'''

'''   
class Solution(object):   #自己想的解法2，双重搜索，n方级
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s==s[::-1]:
            return s
        else:
            length=1
            substr=s[0]
            for i in range(len(s)):
                test=''
                for j in range(i,len(s)):
                    if s[i]==s[j]:
                        test=s[i:j+1]
                        if test==test[::-1]:
                            if len(test)>length:
                                length=len(test)
                                substr=test

            return substr
'''

class Solution(object):    #大神解法1，很快单次搜索n级，用子列的最后一项判断延长
    def longestPalindrome(self,s):
        if s==s[-1]:
            return s

        length=1
        start=0
        for  i in range(len(s)):
            if i-length>=1 and s[i-length-1:i+1]==s[i-length-1:i+1][::-1]:
                start=i-length-1
                length+=2
            if i-length>=0 and s[i-length:i+1]==s[i-length:i+1][::-1]:
                start=i-length
                length+=1
        return s[start:start+length]
        
