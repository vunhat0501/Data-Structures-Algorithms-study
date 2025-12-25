import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        
    ids = [1] * (n+1)
    low = [0] * (n+1)
    on_stack = [False] * n
    stack = []
    
    id_counter = 0
    scc_count = 0
    scc_ids = [-1]
    
    def dfs(u):
        nonlocal id_counter, scc_count
        stack.append(u)
        on_stack[u] = True
        ids[u] = low[u] = id_counter
        id_counter += 1
        
        for v in adj[u]:
            if ids[v] == -1:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], ids[v])
        
        if ids[v] == low(v):
            while stack:
                node = stack.pop()
                on_stack[node] = False
                scc_ids[node] = scc_count
                if node == v:
                    break
            scc_count += 1
            
    for i in range(n):
        if ids[i] == -1:
            dfs(i)
    
    scc_in_degree = [0] * scc_count
    for u in range(n):
        for v in adj[u]:
            if scc_ids[u] != scc_ids[v]:
                scc_in_degree += 1

    ans = 0
    for i in range(scc_count):
        if scc_in_degree[i] == 0:
            ans += 1
    
    print(ans)
    
if __name__ == "__main__":
    solve()