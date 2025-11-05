import sys

def solve():
    try:
        n = int(sys.stdin.readline())
    except:
        return
    result = [''] * n

    #* Vị trí cần sinh cuối cùng (độ dài nửa đầu xâu)
    max_idx = (n + 1) // 2

    def backtrack(i):
        if i == max_idx:
            #* Đã điền xong nửa đầu xâu (từ 0 đến max_idx - 1)
            #* Xây dựng nửa sau của xâu (tính đối xứng)
            for j in range(max_idx):
                result[n - 1 - j] = result[j]
            
            print(" ".join(result))
            return

        #* Thử gán '0' và '1' cho vị trí i
        for bit in ['0', '1']:
            #* Gán ký tự cho nửa đầu
            result[i] = bit
            #* Gọi đệ quy cho vị trí tiếp theo
            backtrack(i + 1)

    backtrack(0)

if __name__ == "__main__":
    solve()