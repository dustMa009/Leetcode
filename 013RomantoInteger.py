class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num=0
        for each in s:
            if each=='I':
                num=num+1
            if each=='V':
                num=num+5
            if each=='X':
                num=num+10
            if each=='L':
                num=num+50
            if each=='C':
                num=num+100
            if each=='D':
                num=num+500
            if each=='M':
                num=num+1000

        if ('IV' in s )or('IX' in s):
            num=num-2
        if ('XL' in s )or('XC' in s):
            num=num-20
        if ('CD' in s )or('CM' in s):
            num=num-200

        return(num)

'''
真是666
class Solution:
def romanToInt(self, s):
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    roman_ixc = {'I':5, 'X':50, 'C':500}
    value = 0
    for i in reversed(s):
        if i in roman_ixc and value >= roman_ixc[i]:
            value -= roman_dict[i]
        else:
            value += roman_dict[i]
    return value
'''
