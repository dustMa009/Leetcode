class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        GE={'0':'','1':'I','2':'II','3':'III','4':'IV',
            '5':'V','6':'VI','7':'VII','8':'VIII','9':'IX'}
        SHI={'0':'','1':'X','2':'XX','3':'XXX','4':'XL',
             '5':'L','6':'LX','7':'LXX','8':'LXXX','9':'XC'}
        BAI={'0':'','1':'C','2':'CC','3':'CCC','4':'CD',
             '5':'D','6':'DC','7':'DCC','8':'DCCC','9':'CM'}
        QIAN={'0':'','1':'M','2':'MM','3':'MMM'}

        result=''
        n=num%10
        result=result+GE[str(n)]
        n=(int(num/10))%10
        result=SHI[str(n)]+result
        n=(int(num/100))%10
        result=BAI[str(n)]+result
        n=(int(num/1000))%10
        result=QIAN[str(n)]+result

        return result
