import sys

# Đặt giá trị vô cùng lớn (lớn hơn trọng số đề bài 10^6)
INF = 10**9

def solve():
    # Đọc dữ liệu nhanh
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)

    n_str = next(iterator, None)
    if not n_str: return
    n = int(n_str)
    m = int(next(iterator))
    q = int(next(iterator))
    
    # Khởi tạo ma trận khoảng cách với giá trị INF
    # Kích thước (N+1)x(N+1) để dùng index 1..N
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # Khoảng cách từ đỉnh đến chính nó là 0
    for i in range(1, n + 1):
        dist[i][i] = 0
        
    # Đọc danh sách cạnh
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        # Nếu có nhiều cạnh nối u, v thì lấy cạnh nhỏ nhất
        dist[u][v] = min(dist[u][v], w)
        
    # --- THUẬT TOÁN FLOYD-WARSHALL (O(N^3)) ---
    for k in range(1, n + 1):          # Duyệt qua các đỉnh trung gian
        for i in range(1, n + 1):      # Duyệt đỉnh đầu
            for j in range(1, n + 1):  # Duyệt đỉnh cuối
                # Công thức Minimax:
                # Để đi i -> j, ta so sánh đường hiện tại
                # với đường đi qua k: i -> k -> j
                # Chi phí qua k là max(chi phí i->k, chi phí k->j)
                val_via_k = max(dist[i][k], dist[k][j])
                
                if dist[i][j] > val_via_k:
                    dist[i][j] = val_via_k
                    
    # Xử lý truy vấn (O(1) mỗi truy vấn)
    for _ in range(q):
        s = int(next(iterator))
        t = int(next(iterator))
        
        res = dist[s][t]
        
        # Nếu vẫn là INF -> Không có đường đi
        if res == INF:
            print(-1)
        else:
            print(res)

if __name__ == "__main__":
    solve()