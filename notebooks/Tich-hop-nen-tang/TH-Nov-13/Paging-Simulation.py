def solve_paging():
    PAGE_SIZE = 1024
    page_table = {
        0: 3,
        1: 7,
        2: 1,
        3: 5
    }

    print(f"\nPAGING")
    print(f"Kich thuoc trang: {PAGE_SIZE} bytes")
    print(f"Bang trang: {page_table}")

    try:
        logic_addr = int(input("Nhap dia chi logic (byte): "))
    except ValueError:
        print("Vui long nhap so nguyen.")
        return

    page_number = logic_addr // PAGE_SIZE
    offset = logic_addr % PAGE_SIZE

    print(f"-> So hieu trang (p): {page_number}")
    print(f"-> Do lech (d): {offset}")

    if page_number in page_table:
        frame_number = page_table[page_number]
        phys_addr = (frame_number * PAGE_SIZE) + offset
        print(f"-> Khung trang (f): {frame_number}")
        print(f"Dia chi vat ly: {phys_addr}")
    else:
        print(f"Loi: Page Fault! Trang {page_number} khong ton tai trong trang")

if __name__ == "__main__":
    solve_paging()