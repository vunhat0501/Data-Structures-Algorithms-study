# ĐƯỜNG ĐI HAMILTON

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
            adj[v].append(u)
            
        visited = [False] * (n+1)
        
        def backtrack(u, count):
            if count == n:
                return True
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    
                    if backtrack(v, count + 1):
                        return True
                    
                    visited[v] = False
            
            return False
        
        found = False
        for i in range(1, n+1):
            visited = [False] * (n+1)
            visited[i] = True
            if backtrack(i, 1):
                found = True
                break
            
        if found:
            print(1)
        else:
            print(0)
if __name__ == "__main__":
    solve()