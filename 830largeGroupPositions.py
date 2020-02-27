class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S)<3:
            return []
        res=[]
        u=1
        S=S+'1'
        for i in range(1,len(S)):
            if S[i]==S[i-1]:
                u+=1
            else:
                if u>2:
                    res.append([i-u,i-1])
                u=1
        return res
