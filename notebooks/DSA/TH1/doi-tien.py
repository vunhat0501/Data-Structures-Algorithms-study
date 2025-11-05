#* thuat toan mid in the middle
import sys

def solve():
    try:
        line = sys.stdin.readline().split()
        if not line: return
        N = int(line[0])
        S = int(line[1])
        T = list(map(int, sys.stdin.readline().split()))
    except:
        return
    if len(T) != N:
        return

    mid = N // 2
    T_A = T[:mid]
    T_B = T[mid:]
    
    sums_A = [] 
    sums_B = []  

    min_count = float('inf')

    #* Backtracking de tao ra cac tong
    def generate_sums(coins, index, current_sum, current_count, result_list):
        if index == len(coins):
            if current_sum <= S:
                result_list.append((current_sum, current_count))
            return

        #* 1. khong chon to tien
        generate_sums(coins, index + 1, current_sum, current_count, result_list)

        #* 2. co chon to tien
        new_sum = current_sum + coins[index]
        if new_sum <= S:
            generate_sums(coins, index + 1, new_sum, current_count + 1, result_list)

    generate_sums(T_A, 0, 0, 0, sums_A)
    generate_sums(T_B, 0, 0, 0, sums_B)
    
    #* sx sums_B theo tong
    sums_B.sort(key=lambda x: x[0])

    optimized_sums_B = {}
    for s, c in sums_B:
        if s not in optimized_sums_B or c < optimized_sums_B[s]:
            optimized_sums_B[s] = c
    
    sorted_opt_B = sorted(optimized_sums_B.items())
    
    # Chuyển danh sách tối ưu hóa thành 2 mảng riêng biệt (tổng và số_tờ)
    B_sums = [item[0] for item in sorted_opt_B]
    B_counts = [item[1] for item in sorted_opt_B]
    len_B = len(B_sums)

    for sum_A, count_A in sums_A:
        target_B = S - sum_A
        
        import bisect
        idx = bisect.bisect_left(B_sums, target_B)
        
        # Nếu tìm thấy target_B (hoặc các phần tử lân cận có cùng tổng)
        if idx < len_B and B_sums[idx] == target_B:
            # Di chuyển về phía trước (nếu có nhiều phần tử cùng tổng) và tìm min_count
            current_min_count_B = float('inf')

            if B_sums[idx] == target_B:
                count_B = B_counts[idx]
                min_count = min(min_count, count_A + count_B)

    if min_count == float('inf'):
        print(-1)
    else:
        print(min_count)

if __name__ == "__main__":
    solve()