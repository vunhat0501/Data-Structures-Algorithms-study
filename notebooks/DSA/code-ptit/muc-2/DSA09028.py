# TÔ MÀU ĐỒ THỊ

import sys
sys.setrecursionlimit(10**6)

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    t = int(next(it))
    
    for _ in range(t):
        n = int(next(it))
        e = int(next(it))
        m = int(next(it))
        
        adj = [[] for _ in range(n+1)]
        for _ in range(e):
            u = int(next(it))
            v = int(next(it))
            adj[u].append(v)
            adj[v].append(u)
            
        colors = [0] * (n+1)
        
        def is_safe(u, c):
            for v in adj[u]:
                if colors[v] == c:
                    return False
            return True
        
        def backtrack(u):
            # Nếu đã duyệt qua đỉnh n (tức là u = n + 1) -> Đã tô xong hết -> Thành công
            if u > n:
                return True
            
            # Thử lần lượt các màu từ 1 đến M cho đỉnh u
            for c in range(1, m + 1):
                if is_safe(u, c):
                    colors[u] = c # Gán màu
                    
                    # Đi tiếp sang đỉnh u + 1
                    if backtrack(u + 1):
                        return True
                    
                    # Nếu đi tiếp không được thì quay lại trả lại màu 0 (Backtrack)
                    colors[u] = 0
            
            return False

        # Bắt đầu tô từ đỉnh 1
        if backtrack(1):
            print("YES")
        else:
            print("NO")
if __name__ == "__main__":
    solve()