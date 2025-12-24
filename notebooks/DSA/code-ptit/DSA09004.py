import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    t = int(next(it))
    for _ in range(t):
        v = int(next(it))
        e = int(next(it))
        u = int(next(it))
        
        adj = [[] for _ in range(v+1)]
        
        for _ in range(e):
            n = int(next(it))
            m = int(next(it))
            
            adj[n].append(m)
            adj[m].append(n)
        
        for i in range(1, v + 1):
                adj[i].sort()
        
        visited = [False] * (v+1)
        stack = [u]
        result = []
        while stack:
            u = stack.pop()
            while not visited[u]:
                visited[u] = True
                result.append(u)
            
                for v in reversed(adj[u]):
                    if not visited[v]:
                        stack.append(v)
    print(*result)
    
if __name__ == "__main__":
    solve()
