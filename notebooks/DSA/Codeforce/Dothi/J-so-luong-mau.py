import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    
    init_colors = []
    for _ in range(n):
        init_colors.append(int(next(it)))
        
    #* khoi tao dsu
    parent = list(range(n+1))
    
    # component_colors[i] lưu dictionary {màu: số_lượng} của nhóm có gốc là i
    # Ban đầu mỗi đỉnh là một nhóm, chứa 1 màu của chính nó
    component_colors = [{} for _ in range(n+1)]
    for i in range(1, n+1):
        color = init_colors[i-1]
        component_colors[i][color] = 1

    # Hàm tìm gốc (Path Compression)
    def find_root(u):
        if parent[u] != u:
            parent[u] = find_root(parent[u])
        return parent[u]

    def union_sets(u, v):
        root_u = find_root(u)
        root_v = find_root(v)
        
        if root_u != root_v:
            # KỸ THUẬT SMALL-TO-LARGE:
            # Luôn gộp tập nhỏ (ít loại màu hơn) vào tập lớn
            if len(component_colors[root_u]) < len(component_colors[root_v]):
                root_u, root_v = root_v, root_u # Đảo để root_u luôn là tập lớn
                
                # Gán cha: root_v nhập vào root_u
                parent[root_v] = root_u
                
                # Duyệt qua các màu của tập nhỏ (root_v) và cộng vào tập lớn (root_u)
                for color, count in component_colors[root_v].items():
                    if color in component_colors[root_u]:
                        component_colors[root_u][color] += count
                    else:
                        component_colors[root_u][color] = count
                # Xóa dictionary của tập con để giải phóng bộ nhớ (Optional nhưng tốt)
                component_colors[root_v].clear()
    
    # Xử lý truy vấn
    results = []
    for _ in range(q):
        type_query = int(next(it))
        x = int(next(it))
        y = int(next(it))
        
        if type_query == 1:
            # Gộp cạnh x, y
            union_sets(x, y)
        else:
            # Đếm số lượng màu y trong vùng chứa x
            root_x = find_root(x)
            # Lấy số lượng từ dictionary của gốc, nếu không có trả về 0
            count = component_colors[root_x].get(y, 0)
            results.append(str(count))
    
    print("\n".join(results))
    
if __name__ == "__main__":
    solve()