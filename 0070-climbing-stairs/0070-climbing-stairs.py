class Solution:
    
    
    
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        
        def go(n) : 
            if n <= 0 :
                return 0
        
            if n == 1 :
                return 1
            if n == 2 :
                return 2

            if n not in memo :
                memo[n] = go(n-1) + go(n-2)
                
            return memo[n]
        
        return go(n)
        
        