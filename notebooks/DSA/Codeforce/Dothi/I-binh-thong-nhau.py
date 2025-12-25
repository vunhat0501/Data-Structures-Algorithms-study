import sys
sys.setrecursionlimit(10**6)

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    n = int(next(it))
    q = int(next(it))
    
    parent = list(range(n+1))
    
    def find_root(u):
        if parent[u] != u:
            parent[u] = find_root(parent[u])
        return parent[u]
    
    def union_sets(u, v):
        root_u = find_root(u)
        root_v = find_root(v)
        
        if root_u != root_v:
            parent[root_u] = root_v
    
    for _ in range(q):
        x = int(next(it))
        y = int(next(it))
        query = int(next(it))
        
        if query == 1:
            union_sets(x, y)
        else:
            if find_root(x) == find_root(y):
                print("YES")
            else:
                print("NO")
    
if __name__ == "__main__":
    solve()
    
    