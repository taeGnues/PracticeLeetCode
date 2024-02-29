class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def bfs(x, y):
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            visited[x][y] = True
            q = deque([[x,y]])
            while q:
                cur_x, cur_y = q.popleft()
                for i in range(4):
                    nx = cur_x + dx[i]
                    ny = cur_y + dy[i]
                    if nx < 0  or ny < 0 or nx >= m or ny >= n:
                        continue
                    if grid[nx][ny]=='0' or visited[nx][ny] :
                        continue

                    visited[nx][ny] = True
                    q.append([nx, ny])

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not visited[i][j] :
                    bfs(i, j)
                    ans += 1
        return ans
                
        