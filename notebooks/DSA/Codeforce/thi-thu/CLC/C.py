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
        end = int(next(it))
        
        adj =[[] for _ in range(n+1)]
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            adj[u].append(v)
            adj[v].append(u)
    
        queue = deque([start])
        dist = [-1] * (n+1)
        dist[start] = 0
        
        found = False
        while queue:
            u = queue.popleft()
            if u == end:
                found = True
                break
            
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        
        if found:
            print(dist[end])
        else:
            print("-1")

if __name__ == "__main__":
    solve()