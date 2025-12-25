# LIỆT KÊ ĐỈNH TRỤ

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
            
        point = []
        
        for i in range(1, n+1):
            visited = [False] * (n+1)
            #* "Xóa" đỉnh i bằng cách đánh dấu nó đã thăm
            visited[i] = True
            
            #* Chọn đỉnh bắt đầu duyệt (khác đỉnh i)
            if i == 1:
                start = 2
            else:
                start = 1
                
            if start > n:
                continue
            
            count = 0
            stack = [start]
            visited[start] = True
            count += 1
            
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
                        count += 1
            
            if count != n-1:
                point.append(i)
                
        print(*point)
    
if __name__ == "__main__":
    solve()