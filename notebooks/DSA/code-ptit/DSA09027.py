# KIỂM TRA ĐƯỜNG ĐI

import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    t = int(next(it))
    
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        
        adj = [[] for _ in range(n+1)]
        
        # Mục tiêu: Chia đồ thị thành các vùng, mỗi vùng có 1 ID riêng
        component_id = [0] * (n+1) # Mảng lưu ID vùng của từng đỉnh
        current_id = 0
        
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            
            adj[u].append(v)
            adj[v].append(u)
            
        # Hàm DFS dùng để đánh dấu tất cả các đỉnh thuộc cùng 1 vùng
        def dfs(start, label):
            stack = [start]
            component_id[start] = current_id
            
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    # Nếu v chưa có nhãn (chưa thuộc vùng nào)
                    if component_id[v] == 0:
                        component_id[v] = label
                        stack.append(v)
        
        # Duyệt qua tất cả các đỉnh để gán nhãn
        for i in range(1, n):
            # Nếu đỉnh i chưa được gán nhãn -> Nó thuộc một vùng mới
            if component_id[i] == 0:
                current_id += 1
                dfs(i, current_id)
        
        # Bây giờ bản đồ đã có ID, trả lời câu hỏi chỉ mất O(1)
        q = int(next(it))
        for _ in range(q):
            x = int(next(it))
            y = int(next(it))
            
            # Chỉ cần so sánh ID vùng của 2 đỉnh
            if component_id[x] == component_id[y]:
                print("YES")
            else:
                print("NO")
    
if __name__ == "__main__":
    solve()