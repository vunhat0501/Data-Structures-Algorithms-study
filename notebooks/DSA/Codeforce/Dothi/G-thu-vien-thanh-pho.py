import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    n = int(next(it))
    m = int(next(it))

    costs = [int(next(it)) for _ in range(n)]
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
        
    total_cost = 0
    visited = [False] * n
    
    def dfs(start):
        stack = [start]
        visited[start] = True
        current_min = costs[start]
        
        while stack:
            u = stack.pop()
            
            if costs[u] < current_min:
                current_min = costs[u]
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        return current_min
    
    for i in range(n):
        if not visited[i]:
            total_cost += dfs(i)
    print(total_cost)
    
if __name__ == "__main__":
    solve()