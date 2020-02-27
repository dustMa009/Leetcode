class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        A=[[0]*len(M[0]) for i in range(len(M))]
        if len(M)==1:       #只有一行
            if len(M[0])==1:
                return M
            A[0][0]=int((M[0][0]+M[0][1])/2)
            A[0][-1]=int((M[0][-2]+M[0][-1])/2)
            for i in range(1,len(M[0])-1):
                A[0][i]=int((M[0][i-1]+M[0][i]+M[0][i+1])/3)
            return A
        
        if len(M[0])==1:       #只有一列
            A[0][0]=int((M[0][0]+M[1][0])/2)
            A[-1][0]=int((M[-2][0]+M[-1][0])/2)
            for i in range(1,len(M)-1):
                A[i][0]=int((M[i-1][0]+M[i][0]+M[i+1][0])/3)
            return A

        #行列数至少为2
        A[0][0]=int((M[0][0]+M[0][1]+M[1][0]+M[1][1])/4)
        A[0][-1]=int((M[0][-2]+M[0][-1]+M[1][-2]+M[1][-1])/4)
        A[-1][0]=int((M[-2][0]+M[-2][1]+M[-1][0]+M[-1][1])/4)
        A[-1][-1]=int((M[-2][-2]+M[-2][-1]+M[-1][-2]+M[-1][-1])/4)

        for i in range(1,len(M)-1):
            A[i][0]=int((M[i-1][0]+M[i][0]+M[i+1][0]+M[i-1][1]+M[i][1]+M[i+1][1])/6)
            A[i][-1]=int((M[i-1][-1]+M[i][-1]+M[i+1][-1]+M[i-1][-2]+M[i][-2]+M[i+1][-2])/6)

        for i in range(1,len(M[0])-1):
            A[0][i]=int((M[0][i-1]+M[0][i]+M[0][i+1]+M[1][i-1]+M[1][i]+M[1][i+1])/6)
            A[-1][i]=int((M[-1][i-1]+M[-1][i]+M[-1][i+1]+M[-2][i-1]+M[-2][i]+M[-2][i+1])/6)

        for i in range(1,len(M)-1):
            for j in range(1,len(M[0])-1):
                A[i][j]=int((M[i-1][j-1]+M[i-1][j]+M[i-1][j+1]+M[i][j-1]+M[i][j]+M[i][j+1]+M[i+1][j-1]+M[i+1][j]+M[i+1][j+1])/9)

        return A
