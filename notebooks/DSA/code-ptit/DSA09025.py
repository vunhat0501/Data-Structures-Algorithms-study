# ĐƯỜNG ĐI THEO DFS VỚI ĐỒ THỊ CÓ HƯỚNG

import sys

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
        
        def dfs(u):
            visited[u] = True
        
            if u == t:
                return True
            
            for v in adj[u]:
                if not visited[v]:
                    parent[v] = u
                    if dfs(v):
                        return True
            return False
        
        
        if dfs(s):
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