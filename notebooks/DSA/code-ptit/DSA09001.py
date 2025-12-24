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
            # adj[v].append(u)
        for i in range(1, n+1):
            adj[i].sort()
            print(f"{i}:", *adj[i])
    
if __name__ == "__main__":
    solve()