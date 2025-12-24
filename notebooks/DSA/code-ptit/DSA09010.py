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
        rev_adj = [[] for _ in range(n+1)]
        
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            
            adj[u].append(v)
            rev_adj[v].append(u)
            
        def bfs(graph, start):
            stack = [start]
            visited = [False] * (n+1)
            visited[start] = True
            count = 0
            
            while stack:
                u = stack.pop()
                count += 1

                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            
            return count
        
        if bfs(adj, 1) != n:
            print("NO")
        else:
            if bfs(rev_adj, 1) != n:
                print("NO")
            else:
                print("YES")

if __name__ == "__main__":
    solve()