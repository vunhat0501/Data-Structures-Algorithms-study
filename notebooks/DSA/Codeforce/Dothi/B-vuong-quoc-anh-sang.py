import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n = int(input().split())
    adj = [[] for _ in range(n)]
    edges = []
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            if row[j] == 1:
                adj[i].append(j)
                if i < j:
                    edges.append((i, j))
    
    def bfs(start, end):
        queue = deque([start])
        visited = [False] * n
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            if u == end:
                return True
            
            for v in adj[u]:
                if start == u and end == v:
                    continue
                
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        return False
    
    count = 0
    for u, v in edges:
        if not bfs(u, v):
            count += 1
    print(count)
    
if __name__ == "__main__":
    solve()

