'''
class Solution(object):  #自己的方法，构思的时间有点长
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        t=''
        a=0
        min1=len(words)+1
        rs=[word1,word2]
        for i in range(len(words)):
            if words[i] in rs:
                if not t:
                    t=words[i]
                    a=i
                    continue
                if words[i]==t:
                    a=i
                else:
                    temp=i-a
                    if temp<min1:
                        min1=temp
                        if min1==1:
                            return 1
                    t=words[i]
                    a=i
        return min1
'''            

class Solution(object):  #好快的方法
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1,i2=float('inf'),float('inf')
        min1=len(words)
        for index,x in enumerate(words):
            if x==word1:
                i1=index
                min1=min(min1,abs(i1-i2))
            if x==word2:
                i2=index
                min1=min(min1,abs(i1-i2))
        return min1
                

