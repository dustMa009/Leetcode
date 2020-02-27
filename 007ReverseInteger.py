class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            a=str(abs(x))
            rx=-int(a[::-1])
        else:
            a=str(x)
            rx=int(a[::-1])
        if abs(rx)>2147483648:
            rx=0
        return(rx)

'''
def reverse(self, x):
    s = cmp(x, 0)
    r = int(`s*x`[::-1])
    return s*r * (r < 2**31)
'''

'''
class Solution(object):
    def reverse(self, x):
        n = cmp(x, 0) * int(str(abs(x))[::-1])
        return n if n.bit_length() < 32 else 0
'''
