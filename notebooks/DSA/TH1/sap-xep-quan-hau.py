import sys

def solve():
    try:
        T = int(sys.stdin.readline())
    except:
        return

    for t in range(1, T + 1):
        # Đọc ma trận bàn cờ 8x8 cho mỗi test
        board = []
        for _ in range(8):
            try:
                line = list(map(int, sys.stdin.readline().split()))
                if len(line) == 8:
                    board.append(line)
                else:
                    return
            except:
                return
        
        global max_score
        max_score = 0
        
        # Các tập hợp để kiểm tra các vị trí bị chiếm
        # col: lưu các cột đã có quân hậu
        # diag1: lưu các giá trị (hàng - cột) của các đường chéo chính đã có quân hậu
        # diag2: lưu các giá trị (hàng + cột) của các đường chéo phụ đã có quân hậu
        col = set()
        diag1 = set() # i - j
        diag2 = set() # i + j

        # Bắt đầu thuật toán quay lui từ hàng 0 với điểm số khởi tạo là 0
        backtrack(0, 0, board, col, diag1, diag2)
        
        # In kết quả theo định dạng yêu cầu
        print(f"Test {t}: {max_score}")

def backtrack(row, current_score, board, col, diag1, diag2):
    global max_score
    
    # 1. Điều kiện dừng: Đã đặt được 8 quân hậu (từ hàng 0 đến 7)
    if row == 8:
        max_score = max(max_score, current_score)
        return

    # 2. Lặp qua tất cả các cột j ở hàng hiện tại
    for j in range(8):
        # 3. Kiểm tra tính an toàn của vị trí (row, j)
        is_safe = (j not in col) and \
                  ((row - j) not in diag1) and \
                  ((row + j) not in diag2)

        if is_safe:
            # 4. Đặt quân (Thực hiện bước tiến)
            col.add(j)
            diag1.add(row - j)
            diag2.add(row + j)
            
            # Gọi đệ quy cho hàng tiếp theo, cập nhật điểm số
            new_score = current_score + board[row][j]
            backtrack(row + 1, new_score, board, col, diag1, diag2)
            
            # 5. Quay lui 
            col.remove(j)
            diag1.remove(row - j)
            diag2.remove(row + j)

if __name__ == "__main__":
    solve()