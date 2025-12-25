# CÂY KHUNG CỦA ĐỒ THỊ THEO THUẬT TOÁN DFS

import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    
    t = int(next(it))
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        start = int(next(it))
        
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            adj[u].append(v)
            adj[v].append(u)
            
        for i in range(1, n+1):
            adj[i].sort()
            
        visited = [False] * (n+1)
        spanning_tree = []
        
        # Stack lưu cặp: (đỉnh cần thăm, cha của nó)
        # Cha = -1 nghĩa là đỉnh gốc, không có cạnh nối tới
        stack = [(start, -1)]
        
        while stack:
            u, parent = stack.pop()
            if not visited[u]:
                visited[u] = True
                
                # Nếu có cha (tức không phải đỉnh xuất phát) -> Lưu cạnh (parent, u)
                if parent != -1:
                    spanning_tree.append(f"{parent} {u}")
                    
                for v in reversed(adj[u]):
                    if not visited[v]:
                        stack.append((v, u))
        if len(spanning_tree) == n-1:
            print("\n".join(spanning_tree))
        else:
            print(-1)
    
if __name__ == "__main__":
    solve()