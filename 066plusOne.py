'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        b=''
        for i in digits:
            b+=str(i)
        b=int(b)+1
        c=[]
        for i in str(b):
            c.append(int(i))
        return c
'''


class Solution(object):   #另一种思路，在列表上直接操作，好像时间一样
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None:
            return None

        if digits[-1]!=9:
            digits[-1]+=1
            return digits
        else:
            pointer=len(digits)-1
            while pointer>0:
                digits[pointer]=0
                pointer-=1
                if digits[pointer]!=9:
                    digits[pointer]+=1
                    return digits
            if digits[0]==9:
                digits[0]=0
                tmp=[1]
                tmp.extend(digits)
                return tmp
            else:
                digits[0]+=1
                return digits
