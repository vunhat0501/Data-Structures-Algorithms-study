import sys

# Hàm kiểm tra cân bằng (Logic cũ của bạn nhưng tối ưu cú pháp một chút)
def isBalanced(s):
    st = []
    # Dùng Dictionary để map cặp ngoặc cho gọn và dễ kiểm tra
    matching = {')': '(', ']': '[', '}': '{'}
    
    for c in s:
        # Nếu là dấu mở ngoac: (, [, {
        if c in "([{":
            st.append(c)
            
        # Nếu là dấu đóng ngoac: ), ], }
        elif c in ")]}":
            # Nếu stack rỗng -> Dư dấu đóng -> False
            if not st:
                return False
            
            # Lấy dấu mở ở đỉnh stack ra so sánh
            top = st.pop()
            
            # Nếu không khớp cặp tương ứng trong dictionary -> False
            if matching[c] != top:
                return False
                
    # Nếu stack còn phần tử -> Dư dấu mở -> False
    # Nếu stack rỗng -> True
    return len(st) == 0

def solve():
    # Đọc toàn bộ dữ liệu từ input chuẩn
    # sys.stdin.read().split() sẽ tự động tách theo khoảng trắng/xuống dòng
    # giúp bỏ qua các vấn đề về ký tự thừa hay dòng trống
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Tạo iterator để duyệt qua từng phần tử input
    iterator = iter(input_data)
    
    try:
        # Đọc số lượng bộ test T
        num_test_cases = int(next(iterator))
        
        for _ in range(num_test_cases):
            s = next(iterator)
            
            # Kiểm tra và in kết quả
            if isBalanced(s):
                print("true")
            else:
                print("false")
                
    except StopIteration:
        return

if __name__ == "__main__":
    solve()