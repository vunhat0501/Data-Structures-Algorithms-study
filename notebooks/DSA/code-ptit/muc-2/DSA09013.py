# LIỆT KÊ CẠNH CẦU BANG DFS TARJAN
import sys

sys.setrecursionlimit(2000)

def solve():
    data = sys.stdin.read().split()
        
    it = iter(data)
    

    test = int(next(it))

    for _ in range(test):
        V = int(next(it))
        E = int(next(it))
        
        adj = [[] for _ in range(V + 1)]
        
        for _ in range(E):
            u = int(next(it))
            v = int(next(it))
            adj[u].append(v)
            adj[v].append(u)

        # Các biến dùng cho thuật toán Tarjan
        disc = [-1] * (V + 1)  # Thời điểm duyệt đến đỉnh
        low = [-1] * (V + 1)   # Thời điểm thấp nhất có thể với tới
        timer = 0
        bridges = []

        def dfs(u, p=-1):
            nonlocal timer
            timer += 1
            disc[u] = low[u] = timer
            
            for v in adj[u]:
                if v == p: # Tránh quay lại cha trực tiếp
                    continue
                
                if disc[v] != -1:
                    # Nếu v đã thăm -> đây là cạnh ngược (back-edge)
                    low[u] = min(low[u], disc[v])
                else:
                    # Nếu v chưa thăm -> đi tiếp (tree-edge)
                    dfs(v, u)
                    # Khi quay lui, cập nhật low[u] theo con v
                    low[u] = min(low[u], low[v])
                    
                    # Điều kiện Cầu: Con v không thể với lên được u hoặc tổ tiên u
                    if low[v] > disc[u]:
                        # Lưu cạnh cầu sao cho u < v
                        if u < v:
                            bridges.append((u, v))
                        else:
                            bridges.append((v, u))

        # Chạy DFS từ đỉnh 1 (vì đề bài cho đồ thị liên thông)
        # Nếu đồ thị không liên thông thì cần vòng lặp for i in range(1, V+1)
        for i in range(1, V + 1):
            if disc[i] == -1:
                dfs(i)

        bridges.sort()

        res_str = []
        for u, v in bridges:
            res_str.append(f"{u} {v}")
        print(*res_str)

if __name__ == "__main__":
    solve()