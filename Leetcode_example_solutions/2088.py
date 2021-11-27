class Solution:
    def countPyramids(self, G):
        m, n, ans = len(G), len(G[0]), 0
        
        @lru_cache(None)
        def dp(i, j, dr):
            if G[i][j] == 1 and 0 <= i + dr < m and j > 0 and j + 1 < n and G[i+dr][j] == 1:
                return min(dp(i+dr, j-1, dr), dp(i+dr, j+1, dr)) + 1
            return G[i][j]
        
        for i, j in product(range(m), range(n)):
            ans += max(0, dp(i, j, 1) - 1)
            ans += max(0, dp(i, j, -1) - 1)
        
        return ans

class Solution2:
    def countPyramids(self, grid: List[List[int]]) -> int:
        
        def count(grid):
            m, n = len(grid), len(grid[0])
            degree = [[0 for _ in range(n)] for _ in range(m)]
            for x in range(1, m):
                for y in range(1, n-1):
                    if grid[x][y] == grid[x-1][y-1] == grid[x-1][y] == grid[x-1][y+1] == 1:
                        degree[x][y] = 1 + min(degree[x-1][y-1], degree[x-1][y], degree[x-1][y+1])
                        
            return sum(sum(row) for row in degree)
        
        return count(grid) + count(grid[::-1])