'''
class Solution(object):   #没利用内置函数，很慢的方法，直接算每一位
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)<=len(b):
            l1=a[::-1]
            l2=b[::-1]
        else:
            l1=b[::-1]
            l2=a[::-1]
        
        jw=0
        result=''
        for i in range(len(l2)):
            if i>=len(l1):
                if jw==0:
                    return (result+l2[i:])[::-1]
                else:
                    jw=int(l2[i])
                    result=result+str(int(l2[i])^1)
            else:
                result=result+str((int(l1[i])+int(l2[i])+jw)%2)
                jw=int((int(l1[i])+int(l2[i])+jw)/2)

        if jw==0:
            return result[::-1]
        else:
            return (result+'1')[::-1]
'''                 

class Solution(object):   #没利用内置函数，很慢的方法，直接算每一位
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2)+int(b,2))[2:]
