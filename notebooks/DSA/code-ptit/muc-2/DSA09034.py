# ĐẾM SỐ AO

import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    it = iter(data)

    n = int(next(it))
    m = int(next(it))
    
    grid = []
    for _ in range(n):
        grid.append(next(it))

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    visited = [[False] * m for _ in range(n)]
    lake = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'W' and not visited[i][j]:
                lake += 1

                queue = deque([(i, j)])
                visited[i][j] = True
                
                while queue:
                    x, y = queue.popleft()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if grid[nx][ny] == 'W' and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
    
    print(lake)

if __name__ == "__main__":
    solve()

