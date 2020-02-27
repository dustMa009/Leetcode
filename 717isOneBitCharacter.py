class Solution(object):  #自己的解法，慢？？？
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits)==1:
            return True
        if bits[-2]==0:
            return True
        a1=(bits[::-1]+[0]).index(0,1)
        if (a1-1)%2==0:
            return True
        return False
