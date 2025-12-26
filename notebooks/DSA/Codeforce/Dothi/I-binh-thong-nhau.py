import sys
sys.setrecursionlimit(10**6)

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    n = int(next(it))
    q = int(next(it))
    
    parent = list(range(n+1))
    rank = [0] * (n+1)
        
    def find_root(u):
        path = []
        while u != parent[u]:
            path.append(u)
            u = parent[u]
        root = u
        for node in path:
            path[node] = root
        return root
    
    def union_sets(u, v):
        root_u = find_root(u)
        root_v = find_root(v)
        
        if root_u != root_v:
            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v]
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
    
    result = []
    for _ in range(q):
        x = int(next(it))
        y = int(next(it))
        query = int(next(it))
        
        if query == 1:
            union_sets(x, y)
        else:
            if find_root(x) == find_root(y):
                result.append("YES")
            else:
                result.append("NO")
    print("\n".join(result))
    
if __name__ == "__main__":
    solve()
    
    