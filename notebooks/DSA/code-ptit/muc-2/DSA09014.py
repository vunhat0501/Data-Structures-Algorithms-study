# KIỂM TRA CHU TRÌNH TRÊN ĐỒ THỊ VÔ HƯỚNG BANG BFS

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
            
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * (n+1)
        parent = [0] * (n+1)
        
        def bfs(start):
            queue = deque([start])
            visited[start] = True
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
                        parent[v] = u
                        
                    # QUAN TRỌNG: Nếu v đã thăm, và v KHÔNG phải là cha của u
                    # Nghĩa là ta gặp lại v qua một đường khác -> Có chu trình
                    elif v != parent[u]:
                        return True
            return False
        
        has_cycle = False
        for i in range(1, n+1):
            if not visited[i]:
                if bfs(i):
                    has_cycle = True
                    break
        if has_cycle:
            print("YES")
        else:
            print("NO")
    
if __name__ == "__main__":
    solve()