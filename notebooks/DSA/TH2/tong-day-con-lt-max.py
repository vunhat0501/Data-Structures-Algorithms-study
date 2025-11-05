import sys

input = sys.stdin.readline

def tinh_tong():
    try:
        n = int(input())
        
        if n == 0:
            print(0)
            return
        
        a = list(map(int, input().split()))
        
        #* Note: Thuat toan Kanade (quy hoach dong)
        #* max_so_far: tong lon nhat tim duoc tu dau mang toi vi tri hien tai
        #* current_max: tong lon nhat cua day con ket thuc tai vi tri hien tai
        
        #* Khoi tao
        max_so_far = a[0]
        current_max = a[0]
        
        for i in range(1, n):
            #* Bat dau day con moi (A[i]) / tiep tuc day con hien tai (current_max + A[i])
            current_max = max(a[i], current_max + a[i])

            max_so_far = max(max_so_far, current_max)
            
        print(max_so_far)
        
    except EOFError:
        pass
    except ValueError:
        pass
    
try:
    t = int(input())
    
    for _ in range(t):
        tinh_tong()

except ValueError:
    pass