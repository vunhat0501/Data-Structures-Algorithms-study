import sys

def solve():
    #* Chu trình Euler: Tồn tại khi và chỉ khi với mọi đỉnh, bán bậc vào bằng bán bậc ra.
    #* In[u] == Out[u] (với mọi u)
    data = sys.stdin.read().split()
    it = iter(data)
    
    t = int(next(it))
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        
        balance = [0] * (n+1)
        
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            
            #* canh u -> v
            balance[u] += 1
            balance[v] -= 1
            
        # Kiểm tra điều kiện Chu trình Euler: In == Out với mọi đỉnh
        # Tức là balance[i] phải bằng 0 với mọi i
        euler_cycle = True
        for i in range(1, n+1):
            if balance[i] != 0:
                euler_cycle = False
                break
            
        if euler_cycle:
            print(1)
        else:
            print(0)
if __name__ == "__main__":
    solve()