class Solution(object):   
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        a5=0

        while n>4:
            n=int(n/5)
            a5=a5+n
        return a5
                
