import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    T = int(next(it))
    for _ in range(T):
        n = int(next(it))
        m = int(next(it))
        s = int(next(it))
        t = int(next(it))
        
        adj = [[] for _ in range(n+1)]
        
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            
            adj[u].append(v)
            
        for i in range(n+1):
            adj[i].sort()
            
        visited = [False] * (n+1)
        parent = [0] * (n+1)
        
        def bfs(start, end):
            queue = deque([start])
            visited[start] = True
            parent[start] = 0
            
            while queue:
                u = queue.popleft()
                if u == end:
                    return True
                
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        parent[v] = u
                        queue.append(v)
            return False
        
        if bfs(s, t):
            path = []
            current = t
            while current != 0:
                path.append(current)
                if current == s:
                    break
                current = parent[current]
            path.reverse()
            print(*path)
        else:
            print(-1)
    
if __name__ == "__main__":
    solve()