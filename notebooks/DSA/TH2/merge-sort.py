import sys

def merge(arr, aux, left, mid, right):
    #* Khoi tao mang con
    # n1 = mid - left + 1
    # n2 = right - mid
    
    for k in range(left, right + 1):
        aux[k] = arr[k]
    
    #* Tao mang tam thoi chi chua cac phan tu 0
    # L = [0] * (n1)
    # R = [0] * (n2)
    
    #* Sao chep gia tri tu arr vao mang tam thoi
    # for i in range(n1):
    #     L[i] = arr[left + i]
    # for j in range(n2):
    #     R[j] = arr[mid + 1 + j]
        
    #* con tro
    i = left
    j = mid + 1
    k = left
    
    #* Sao chep phan tu tu aux ve arr
    while i <= mid and j <= right:
        if aux[i] <= aux[j]:
            arr[k] = aux[i]
            i += 1
        else:
            arr[k] = aux[j]
            j += 1
        k += 1
        
    #* Sao chep phan con lai
    while i <= mid:
        arr[k] = aux[i]
        i += 1
        k += 1
        
    while j <= right:
        arr[k] = aux[j]
        j += 1
        k += 1
    
    # #* Merge gia tri tu mang tam thoi ve arr goc
    # while i < n1 and j < n2:
    #     if L[i] <= R[j]:
    #         arr[k] = L[i]
    #         i += 1
    #     else:
    #         arr[k] = R[j]
    #         j += 1
    #     k += 1
        
    # #* Sao chep nhung phan tu con lai trong L[]
    # while i < n1:
    #     arr[k] = L[i]
    #     i += 1
    #     k += 1
        
    # #* Sao chep nhung phan tu con lai trong R[]
    # while j < n2:
    #     arr[k] = R[j]
    #     j += 1
    #     k += 1
        
def merge_sort(arr, aux, left, right):
    if left < right:
        mid = (left + right) // 2
        
        #* De quy
        merge_sort(arr, aux, left, mid)
        merge_sort(arr, aux, mid + 1, right)
        
        #* Gop mang sau de quy
        merge(arr, aux, left, mid, right)
        
try:
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        aux = [0] * n
        
        merge_sort(a, aux, 0, n - 1)

        print(*a)

except ValueError:
    pass
except EOFError:
    pass