import sys
from collections import deque
input = sys.stdin.readline

def solve(n, u, v, arr):
    #* khoi tao prefix sum
    prefix_sum = [0] * (n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i] 
    
    #* khoi tao bien max sum = - inf
    max_sum = -float('inf')
    
    #* khoi tao deque rong
    dq = deque()

    #* duyet i chay tu u den n
    for i in range(u, n+1):
        
    #* diem bat dau moi co the them vao cua so hay khong: k = i -u 
        k = i - u

        #* cap nhat deque voi k
        #* while deque khong rong va S[deque.back()] > S[k]: pop.back
        #* Duy trì tính đơn điệu tăng: Loại bỏ các phần tử lớn hơn hoặc bằng S[k]
        #* (Vì k mới hơn, nên nếu S[k] nhỏ hơn thì các số trước đó vô dụng)
        while dq and prefix_sum[dq[-1]] >= prefix_sum[k]:
            dq.pop()
            
        #* push k vao deque
        dq.append(k)
        
        #* loai bo diem qua han
        #* bat dau tu i - v. neu deque.front() < i - u: pop.front()
        while dq and dq[0] < i - v:
            dq.popleft()
            
        #* tinh current_sum = S[i] - S[deque.front()]
        if dq:
            current_sum = prefix_sum[i] - prefix_sum[dq[0]]
            if current_sum > max_sum:
                #* cap nhat max_sum = max(max_sum, current_sum)
                max_sum = current_sum
    return(max_sum)
n, u, v = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(solve(n, u, v, arr))

