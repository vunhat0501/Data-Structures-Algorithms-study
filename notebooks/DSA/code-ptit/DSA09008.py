import sys

def solve():
    input_data = sys.stdin.read().split()
    it = iter(input_data)

    t = int(next(it))

    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        
        adj = [[] for _ in range(n + 1)]
        
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            
            #* kiem tra tranh IndexError (trong truong hop de bai cho u > n)
            #* bai can, bai khong can.
            if 1 <= u <= n and 1 <= v <= n:
                adj[u].append(v)
                adj[v].append(u)
        
        visited = [False] * (n + 1)
        count = 0
        
        def dfs_check(start_node):
            stack = [start_node]
            visited[start_node] = True
            
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
        
        for i in range(1, n + 1):
            if not visited[i]:
                count += 1
                dfs_check(i)
                
        print(count)

if __name__ == "__main__":
    solve()