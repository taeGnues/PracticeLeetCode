



class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        nums = [i for i in range(1, n+1)]
        ans = []
        def go(curr):    
            if len(curr) == len(nums):
                ans.append(curr[:])
                return 
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    go(curr)
                    if len(ans)>=k:
                        return
                    curr.pop()
                    
        go([])
        
        return ''.join(map(str, ans[k-1]))
        