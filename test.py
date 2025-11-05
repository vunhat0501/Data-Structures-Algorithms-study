def solve_prefix_sum():
    """
    Hàm giải quyết bài toán bằng Tổng tiền tố và Bảng băm.
    """
    try:
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
    except (ValueError, IndexError):
        return

    prefix_sums = {0} # Thêm 0 để xử lý trường hợp dãy con bắt đầu từ chỉ số 0
    current_sum = 0
    found = False

    for num in a:
        current_sum += num
        # Kiểm tra xem (current_sum - k) có trong các tổng tiền tố đã gặp không
        if (current_sum - k) in prefix_sums:
            found = True
            break
        # Thêm tổng tiền tố hiện tại vào set
        prefix_sums.add(current_sum)

    if found:
        print("YES")
    else:
        print("NO")

# Xử lý nhập liệu cho nhiều bộ test
try:
    num_tests = int(input())
    for _ in range(num_tests):
        solve_prefix_sum()
except (ValueError, IndexError):
    pass