# TÌM SỐ THÀNH PHẦN LIÊN THÔNG VỚI BFS

import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    t = int(next(it))
    
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        
        adj = [[] for _ in range(n+1)]
        
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            
            if 1 <= u <= n and 1 <= v <= n:
                adj[u].append(v)
                adj[v].append(u)
        
        visited = [False] * (n+1)
        count = 0
        
        def bfs_check(start_node):
            queue = deque([start_node])
            visited[start_node] = True
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
        
        for i in range(1, n+1):
            if not visited[i]:
                count += 1
                bfs_check(i)
        
        print(count)
    
if __name__ == "__main__":
    solve()