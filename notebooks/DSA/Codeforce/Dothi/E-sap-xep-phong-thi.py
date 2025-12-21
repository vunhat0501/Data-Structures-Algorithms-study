import sys
input = sys.stdin.readline

def solve():
    n, m = list(map(int, input().split()))
    
    #* khoi tao adj
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = list(map(int, input().split()))
        adj[u].append(v)
        adj[v].append(u)
    
    #* khoi tao visited chua sv da xep nhom
    visited = [False] * (n+1)
    max_size = 0
    
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
    
    for i in range(1, n+1):
        if not visited[i]:
            current = dfs(i)
            if current > max_size:
                max_size = current
    print(max_size)
    
if __name__ == "__main__":
    solve()