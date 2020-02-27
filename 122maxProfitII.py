class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy=prices[0]
        profit=0
        sum1=0
        for each in prices:
            if each<buy+profit:
                sum1=sum1+profit
                buy=each
                profit=0
            if each>=buy+profit:
                profit=each-buy

        return sum1+profit


'''
class Solution(object):      #更直接的方法
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        sum1=0
        for i in range(1,len(prices)):
            t=prices[i]-prices[i-1]
            if t>0:
                sum1=sum1+t

        return sum1
'''
