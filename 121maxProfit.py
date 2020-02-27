class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        start=prices[0]
        max1=0
        for each in prices:
            if each<start:
                start=each
            if each>start+max1:
                max1=each-start

        return max1
            
