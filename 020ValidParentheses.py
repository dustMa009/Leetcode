class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while ('()' in s) or ('[]' in s) or ('{}' in s):
            s=s.replace('()','')
            s=s.replace('[]','')
            s=s.replace('{}','')

        return s==''


'''
很快的解答，666
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = { ')':'(', ']':'[', '}':'{' }
        stackBox = []
        for i in s:
            if i not in match:
                stackBox.append(i)
            else:
                if len(stackBox)==0 or stackBox[-1] != match[i]:
                    return False
                stackBox.pop()
        return len(stackBox)==0
'''
