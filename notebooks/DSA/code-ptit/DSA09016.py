# KIỂM TRA CHU TRÌNH TRÊN ĐỒ THỊ CÓ HƯỚNG VỚI DFS

import sys
sys.setrecursionlimit(10**6)

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
        
        color = [0] * (n+1)
        
        def dfs(u):
            color[u] = 1
            
            for v in adj[u]:
                if color[v] == 1:
                    return True
                if color[v] == 0:
                    if dfs(v):
                        return True
            
            color[u] = 2
            return False
        
        has_cycle = False
        for i in range(1, n+1):
            if color[i] == 0:
                if dfs(i):
                    has_cycle = True
                    break
        
        if has_cycle:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()