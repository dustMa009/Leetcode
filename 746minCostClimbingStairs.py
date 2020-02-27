class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        if n==2:
            return min(cost)
        if n==3:
            return min(cost[0]+cost[2],cost[1])
        i=n-2
        s1=0
        s2=cost[n-1]
        while i>=2:
            s1+=cost[i]
            if s1<=s2:
                return Solution.minCostClimbingStairs(self,cost[0:i])+s1
            else:
                s1,s2=s2,s1
                i-=1
        return min(s1+cost[1],s2+cost[0])
        
