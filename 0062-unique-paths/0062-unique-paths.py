class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        
        def go(cx, cy) :
            if cx == m-1 and cy == n-1 :
                return 1
            
            if cx >= m or cy >= n :
                return 0
            
            if (cx, cy) not in memo :
                memo[(cx,cy)] = go(cx + 1, cy) + go(cx, cy+1)
            
            return memo[(cx,cy)]
        
        return go(0, 0)