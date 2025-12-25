# KIỂM TRA CHU TRÌNH TRÊN ĐỒ THỊ CÓ HƯỚNG BANG BFS

import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    t = int(next(it))
    
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        
        adj = [[] for _ in range(n+1)]
        in_degree = [0] * (n + 1)
        
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            
            adj[u].append(v)
            in_degree[v] += 1
        
        # --- THUẬT TOÁN KAHN (BFS) ---
        queue = deque()
        
        # 1. Nạp tất cả đỉnh có bậc vào = 0 vào hàng đợi
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                queue.append(i)
        
        cnt_visited = 0 # Đếm số đỉnh đã được duyệt
        
        while queue:
            u = queue.popleft()
            cnt_visited += 1
            
            # Duyệt các đỉnh kề
            for v in adj[u]:
                # Giả vờ xóa đỉnh u đi, thì v sẽ mất 1 mũi tên trỏ vào
                in_degree[v] -= 1
                
                # Nếu v không còn ai trỏ vào nữa, thì nạp v vào hàng đợi
                if in_degree[v] == 0:
                    queue.append(v)
        
        # Nếu số đỉnh duyệt được < N -> Có chu trình (vì các đỉnh trong chu trình không bao giờ có in_degree về 0)
        if cnt_visited < n:
            print("YES")
        else:
            print("NO")
            
if __name__ == "__main__":
    solve()