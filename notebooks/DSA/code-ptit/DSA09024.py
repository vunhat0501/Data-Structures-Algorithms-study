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
        edges = []
        
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            
            adj[u].append(v)
        
        for i in range(1, n + 1):
            adj[i].sort()
        
        path = []

        queue = deque([start])
        visited = [False] * (n+1)
        visited[start] = True
            
        while queue:
            u = queue.popleft()
            path.append(str(u))
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        
        print(" ".join(path))
    
if __name__ == "__main__":
    solve()

