# KIỂM TRA ĐỒ THỊ CÓ PHẢI LÀ CÂY HAY KHÔNG

import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    t = int(next(it))
    
    for _ in range(t):
        n = int(next(it))
        
        adj = [[] for _ in range(n+1)]
        for _ in range(n-1):
            u = int(next(it))
            v = int(next(it))
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * (n+1)
        
        def dfs(u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)
        
        dfs(1)
        
        is_connected = True
        
        for i in range(1, n+1):
            if not visited[i]:
                is_connected = False
                break
        
        if is_connected:
            print("YES")
        else:
            print("NO")
    
if __name__ == "__main__":
    solve()