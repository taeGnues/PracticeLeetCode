class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        
        def go(n) :
            
            if n <= 1 :
                return 0
                        
            if n not in memo :
                memo[n] = min(go(n-1) + cost[n-1], go(n-2) + cost[n-2])
                
            return memo[n]
        
        return go(len(cost))
    
    