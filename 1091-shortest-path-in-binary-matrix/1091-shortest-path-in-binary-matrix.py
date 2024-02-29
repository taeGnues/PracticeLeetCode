from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[0]*n for _ in range(n)]
        dy = [1, 1, 1, 0, 0, -1, -1, -1]
        dx = [0, 1, -1, 1, -1, 0, -1, 1]
        
        if grid[0][0]==1 :
            return -1
        q = deque([[0, 0]])
        visited[0][0] = 1
        
        while q :
            cur_y, cur_x = q.popleft()
            
            for i in range(8):
                ny = cur_y + dy[i]
                nx = cur_x + dx[i]
                
                if ny < 0 or nx < 0 or ny >= n or nx >= n :
                    continue
                if visited[ny][nx] != 0 or grid[ny][nx] == 1 :
                    continue
                
                q.append([ny, nx])
                visited[ny][nx] = visited[cur_y][cur_x] + 1
        
        return -1 if visited[n-1][n-1]==0 else visited[n-1][n-1]
        