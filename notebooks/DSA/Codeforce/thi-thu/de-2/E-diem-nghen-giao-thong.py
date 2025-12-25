import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    t = int(next(it))
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        x = int(next(it))
        y = int(next(it))
        
        x-= 1
        y-= 1
        
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            adj[u].append(v)
            adj[v].append(u)
            
        def bfs(start, end, blocked):
            queue = deque([start])
            visited = [False] * (n+1)
            visited[start] = True

            while queue:
                u = queue.popleft()
                if u == end:
                    return True
                for v in adj[u]:
                    if not visited[v] and v != blocked:
                        visited[v] = True
                        queue.append(v)
            return False

        count = 0
        for i in range(n):
            if i == x or i == y:
                continue
            if not bfs(x, y, blocked=i):
                count += 1
        print(count)
    
if __name__ == "__main__":
    solve()