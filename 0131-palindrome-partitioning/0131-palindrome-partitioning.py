
#7:17

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        def go(st, v):
            
            if "".join(v)==s:
                for i in v :
                    if i[::-1] != i:
                        return 
                ans.append(v[:])
                return
            
            for i in range(st+1, len(s)): # 0, 1, 2
                v.append(s[st+1:i+1]) 
                go(i, v)
                v.pop()

        go(-1, [])
        
        return ans