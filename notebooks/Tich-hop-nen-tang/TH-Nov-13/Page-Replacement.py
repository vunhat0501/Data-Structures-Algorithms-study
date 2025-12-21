def solve_page_replacement():
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
    capacity = 3
    
    print(f"\nPAGE REPLACEMENT")
    print(f"Chuoi tham chieu: {pages}")
    print(f"So khung (Frames): {capacity}")

    def run_fifo(ref_pages, n):
        memory = []
        page_faults = 0
        print("\n[FIFO Simulation]")
        for page in ref_pages:
            if page not in memory:
                page_faults += 1
                if len(memory) < n:
                    memory.append(page)
                else:
                    removed = memory.pop(0) 
                    memory.append(page)
                print(f"Truy cap {page}: Miss -> Memory: {memory}")
            else:
                print(f"Truy cap {page}: Hit  -> Memory: {memory}")
        return page_faults

    def run_lru(ref_pages, n):
        memory = []
        page_faults = 0
        print("\n[LRU Simulation]")
        for page in ref_pages:
            if page not in memory:
                page_faults += 1
                if len(memory) < n:
                    memory.append(page)
                else:
                    removed = memory.pop(0) 
                    memory.append(page)
                print(f"Truy cap {page}: Miss -> Memory: {memory}")
            else:
                memory.remove(page)
                memory.append(page)
                print(f"Truy cap {page}: Hit  -> Memory: {memory}")
        return page_faults

    pf_fifo = run_fifo(pages, capacity)
    pf_lru = run_lru(pages, capacity)

    print(f"\n Ket qua")
    print(f"So loi trang (Page Faults) cua FIFO: {pf_fifo}")
    print(f"So loi trang (Page Faults) cua LRU : {pf_lru}")

if __name__ == "__main__":
    solve_page_replacement()