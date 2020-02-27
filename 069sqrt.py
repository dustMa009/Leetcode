import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))

'''
class Solution(object):   #题目的意思好像不让用sqrt，别人用的0.5次方方法
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=x**0.5
        return int(a)
'''
