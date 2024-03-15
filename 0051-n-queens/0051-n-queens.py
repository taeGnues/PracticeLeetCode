class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        qns_poss = []
        bd = [0]*n
        vis = [False]*n
        # bd[i] = j 는, i열에 j행을 선택했다는 의미.

        def check(nt): # 해당 열에 대해 있는 퀀이 올바른 위치인지 체크하기
            for i in range(nt):
                if bd[i]==bd[nt] or abs(bd[i]-bd[nt]) == abs(i-nt):
                    return False
            return True


        def go(depth, curr):
            
            if depth == n : # 선택된 열이 끝에 도달함.
                qns_poss.append(curr[:])
                return
            
            for i in range(n): # 해당depth번째 열에서 모든행 순회하기
                if vis[i]==False : # 해당 열 방문하지 않았다면
                    bd[depth] = i # depth, i 퀸 두기
                    
                    if check(depth): 
                        vis[i] = True # 해당 열 방문표시
                        curr.append((depth, i))
                        go(depth+1, curr)
                        curr.pop()
                        vis[i] = False
            
            return
        
        
        go(0, [])
        print(len(qns_poss))
        
        for i in qns_poss:
            bd = [['.']*n for _ in range(n)]
            for j in i:
                bd[j[0]][j[1]] = 'Q'
            ans.append(bd)
        
        total_ans = []
        for i in ans :
            tmp = []
            for j in i :
                tmp.append(''.join(j))
            total_ans.append(tmp)
        print(total_ans)
        
        return total_ans
        
            
            
            