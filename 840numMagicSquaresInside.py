class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)<3 or len(grid[0])<3:
            return 0
        sum1=0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j]!=5:
                    continue
                if {grid[i-1][j],grid[i][j-1],grid[i][j+1],grid[i+1][j]}!={1,3,7,9} or {grid[i-1][j-1],grid[i-1][j+1],grid[i+1][j-1],grid[i+1][j+1]}!={2,4,6,8}:
                    continue
                if grid[i-1][j-1]+grid[i-1][j]+grid[i-1][j+1]!=15 or grid[i][j-1]+grid[i][j]+grid[i][j+1]!=15:
                    continue
                if grid[i-1][j-1]+grid[i][j-1]+grid[i+1][j-1]!=15 or grid[i-1][j]+grid[i][j]+grid[i+1][j]!=15:
                    continue
                sum1+=1
        return sum1
                      
                        
