import sys

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
        
        for i in range(1, n+1):
            visited[i] = True
            visited = [False] * (n+1)
            component_count = 0
            
            for j in range(1, n+1):
                if not visited[j]:
                    component_count += 1

                stack = [j]
                visited[j] = True
                
                while stack:
                    u = stack.pop()
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
        print(component_count)
    
if __name__ == "__main__":
    solve()