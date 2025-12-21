import sys
from collections import deque
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, m, x, y = list(map(int, input().split()))
        
        x -= 1
        y -= 1
        
        adj = [[] for _ in range(n)]
        
        for _ in range(m):
            u, v = list(map(int, input().split()))
            adj[u-1].append(v-1)
            
        def bfs(start, end, blocked_node):
            queue = deque([start])
            visited = [False] * n
            visited[start] = True
            
            while queue:
                u = queue.popleft()
                if u == end:
                    return True
                
                for v in adj[u]:
                    if not visited[v] and v != blocked_node:
                        visited[v] = True
                        queue.append(v)
            
            return False
        
        count = 0
        for i in range(n):
            if i == x or i == y:
                continue
            if not bfs(x, y, blocked_node=i):
                count += 1
        print(count)
        
if __name__ == "__main__":
    solve()