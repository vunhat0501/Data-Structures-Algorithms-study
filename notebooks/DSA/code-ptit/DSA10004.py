import sys

def solve():
    #* Chu trình Euler (Euler Cycle): Tồn tại khi và chỉ khi TẤT CẢ các đỉnh đều có bậc CHẴN. (Output = 2)
    #* Đường đi Euler (Euler Path): Tồn tại khi và chỉ khi có ĐÚNG 2 đỉnh có bậc LẺ, còn lại là bậc chẵn. (Output = 1)
    #* Không có cả hai: Các trường hợp còn lại (ví dụ có 4 đỉnh bậc lẻ, 1 đỉnh bậc lẻ...). (Output = 0)
    data = sys.stdin.read().split()
    it = iter(data)
    
    T = int(next(it))
    for _ in range(T):
        n = int(next(it))
        m = int(next(it))
        
        # Mảng lưu bậc của các đỉnh (Degree array)
        degree = [0] * (n+1)
        
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            
            # Đồ thị vô hướng: cạnh nối u-v làm tăng bậc của cả u và v
            degree[u] += 1
            degree[v] += 1
            
        # Đếm số đỉnh có bậc LẺ
        odd_count = 0
        for i in range(1, n+1):
            if degree[i] % 2 != 0:
                odd_count += 1
        
        # Kiểm tra điều kiện Euler
        if odd_count == 0:
            print(2) # Chu trình Euler (Tất cả chẵn)
        elif odd_count == 2:
            print(1) # Đường đi Euler (Có đúng 2 đỉnh lẻ)
        else:
            print(0) # Không có

if __name__ == "__main__":
    solve()