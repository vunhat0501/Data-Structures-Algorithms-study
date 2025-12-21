import copy

def solve_memory_allocation():
    initial_blocks = [3, 8, 7, 10]
    print(f"Danh sach vung nho ban dau (MB): {initial_blocks}")
    
    try:
        process_size = float(input("Nhap kich thuoc tien trinh can cap phat (MB): "))
    except ValueError:
        print("Vui long nhap so hop le.")
        return

    def first_fit(blocks, size):
        for i, capacity in enumerate(blocks):
            if capacity >= size:
                return i  
        return -1

    def best_fit(blocks, size):
        best_idx = -1
        min_diff = float('inf')
        for i, capacity in enumerate(blocks):
            if capacity >= size:
                diff = capacity - size
                if diff < min_diff:
                    min_diff = diff
                    best_idx = i
        return best_idx

    def worst_fit(blocks, size):
        worst_idx = -1
        max_diff = -1
        for i, capacity in enumerate(blocks):
            if capacity >= size:
                diff = capacity - size
                if diff > max_diff:
                    max_diff = diff
                    worst_idx = i
        return worst_idx

    strategies = {
        "First Fit": first_fit,
        "Best Fit": best_fit,
        "Worst Fit": worst_fit
    }

    print("\nKet qua")
    for name, func in strategies.items():
        blocks = copy.deepcopy(initial_blocks) 
        idx = func(blocks, process_size)
        
        if idx != -1:
            original_size = blocks[idx]
            remaining = original_size - process_size
            print(f"[{name}]: Cap phat tai Block chi so {idx} (kich thuoc {original_size}MB). Du: {remaining}MB")
        else:
            print(f"[{name}]: Khong du bo nho de cap phat")

if __name__ == "__main__":
    solve_memory_allocation()