class Solution(object):
    def valuee(self,x1,x2,x3,x4):
        m1=-1
        t1=(x1*10+x2)*60+x3*10+x4
        ans=""
        if m1<t1<1440 and x3<6:
            m1=t1
            ans=str(x1)+str(x2)+":"+str(x3)+str(x4)

        t2=(x1*10+x2)*60+x4*10+x3
        if m1<t2<1440 and x4<6:
            m1=t2
            ans=str(x1)+str(x2)+":"+str(x4)+str(x3)

        t3=(x2*10+x1)*60+x3*10+x4
        if m1<t3<1440 and x3<6:
            m1=t3
            ans=str(x2)+str(x1)+":"+str(x3)+str(x4)

        t4=(x2*10+x1)*60+x4*10+x3
        if m1<t4<1440 and x4<6:
            m1=t4
            ans=str(x2)+str(x1)+":"+str(x4)+str(x3)

        return (m1,ans)
    
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        ans=[]
        ans.append(self.valuee(A[0],A[1],A[2],A[3]))
        ans.append(self.valuee(A[0],A[2],A[1],A[3]))
        ans.append(self.valuee(A[0],A[3],A[1],A[2]))
        ans.append(self.valuee(A[2],A[1],A[0],A[3]))
        ans.append(self.valuee(A[3],A[1],A[2],A[0]))
        ans.append(self.valuee(A[2],A[3],A[0],A[1]))

        ans.sort()
        return ans[-1][1]
        
