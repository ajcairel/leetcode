class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        cur=0
        dp0=cost[0]
        print('first dp: ', dp0)
        
      
        dp1 = cost[1]

        
        for i in range(2, len(cost)):
            cur = cost[i] + min(dp0, dp1)
            dp0 = dp1
            dp1 = cur
            print('i: ', i)
            print('cur: ', cur)
            print('dp0: ', dp0)
            print('dp1: ', dp1)
            
        return min(dp0, dp1)