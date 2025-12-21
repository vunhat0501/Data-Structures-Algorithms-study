import sys
input = sys.stdin.readline

def solve():
    n, m = list(map(int, input().split()))
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = list(map(int, input().split()))
        adj[u].append(v)
        adj[v].append(u)
        
    visited = [False] * (n+1)
    
    def dfs(u):
        stack = [u]
        visited[u] = True
        count = 0
        while stack:
            u = stack.pop()
            count += 1
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        return count
    
    size_comp1 = dfs(1)
    max_other_comp = 0
    for i in range(2, n+1):
        if not visited[i]:
            current_comp = dfs(i)
            if current_comp > max_other_comp:
                max_other_comp = current_comp
    print(size_comp1 + max_other_comp)
    
if __name__ == "__main__":
    solve()