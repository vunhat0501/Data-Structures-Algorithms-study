import sys

input = sys.stdin.readline

def binary_search(arr, n, k):
    left = 0
    right = n - 1
    
    while left <= right:
        #* Tinh chi so giua
        mid = (left + right) // 2
        
        #* Kiem tra neu K o chinh giua
        if arr[mid] == k:
            return mid + 1  
        
        #* K > mid => bỏ qua nửa bên trái
        elif arr[mid] < k:
            left = mid + 1
            
        #* K < mid, bo nua phai
        else:
            right = mid - 1
            
    #* Khong tim thay, tra ve NO
    return "NO"

try:
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        result = binary_search(a, n, k)
        print(result)

except ValueError:
    pass
except EOFError:
    pass