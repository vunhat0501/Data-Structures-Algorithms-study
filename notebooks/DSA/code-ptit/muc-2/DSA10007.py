# CÂY KHUNG CỦA ĐỒ THỊ THEO THUẬT TOÁN BFS

import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    t = int(next(it))
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        start = int(next(it))
        
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            adj[u].append(v)
            adj[v].append(u)
            
        for i in range(1, n+1):
            adj[i].sort()
            
        visited = [False] * (n+1)
        spanning_tree = []
        
        queue = deque([start])
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    spanning_tree.append(f"{u} {v}")
                    queue.append(v)
        if len(spanning_tree) == n - 1:
                print("\n".join(spanning_tree))
        else:
            print(-1)
            
if __name__ == "__main__":
    solve()