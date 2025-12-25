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
            
        disc = [0] * (n + 1)  # Thời gian phát hiện
        low = [0] * (n + 1)   # Low-link value
        timer = 0
        
        # Mảng lưu kết quả: result[u] là số TPLT nếu bỏ u
        # Mặc định nếu bỏ u đi, ít nhất đồ thị vẫn còn 1 phần (nếu đồ thị ban đầu liên thông)
        # Nếu u không phải đỉnh trụ, result[u] = 1 (số TPLT ban đầu)
        result = [1] * (n + 1)
        
        # Đếm số TPLT ban đầu của đồ thị (đề phòng đồ thị gốc đã rời rạc)
        original_components = 0
        visited = [False] * (n + 1)
        
        def dfs_tarjan(u, p=-1):
            nonlocal timer
            timer += 1
            disc[u] = low[u] = timer
            visited[u] = True
            
            children = 0 # Đếm số con trực tiếp trong cây DFS
            
            for v in adj[u]:
                if v == p:
                    continue 
                
                if visited[v]:
                    # Cạnh ngược (Back-edge): cập nhật low[u]
                    low[u] = min(low[u], disc[v])
                else:
                    children += 1
                    dfs_tarjan(v, u)
                    
                    # Cạnh xuôi (Tree-edge): lấy low từ con
                    low[u] = min(low[u], low[v])
                    
                    # KIỂM TRA ĐIỀU KIỆN ĐỈNH TRỤ
                    if p != -1 and low[v] >= disc[u]:
                        # Nếu u không phải gốc và con v không leo lên trên u được
                        # Thì nhánh v sẽ bị tách ra -> Tăng số TPLT lên 1
                        result[u] += 1
            
            # Trường hợp đặc biệt: Nếu u là Gốc của cây DFS
            if p == -1:
                # Nếu bỏ gốc, số TPLT = số nhánh con
                result[u] = children
                
        # Chạy thuật toán qua tất cả các đỉnh (đề phòng đồ thị ngắt quãng)
        for i in range(1, n + 1):
            if not visited[i]:
                original_components += 1
                # Gốc cây DFS thì p = -1
                dfs_tarjan(i, -1)
                # Sau khi chạy xong 1 TPLT gốc, nếu số con của gốc < 1 thì khi xóa nó, TPLT giảm đi 1 (mất luôn vùng đó)
                # Tuy nhiên đề bài thường hỏi số vùng CÒN LẠI, logic trên đã cover phần lớn.
        
        # In kết quả cho từng đỉnh
        # Lưu ý: Logic trên tính số mảnh vỡ ra từ 1 TPLT gốc.
        # Nếu đồ thị ban đầu có K vùng (original_components), 
        # thì tổng số vùng sau khi xóa u = (result[u] + K - 1).
        
        final_output = []
        for i in range(1, n + 1):
            # result[i] là số mảnh vỡ ra của vùng chứa i
            # Ta cộng thêm các vùng rời rạc khác không bị ảnh hưởng
            ans = result[i] + (original_components - 1)
            final_output.append(str(ans))
        
        print("\n".join(final_output)) # In mỗi số một dòng hoặc print(" ".join(...)) tùy đề
        
if __name__ == "__main__":
    solve()