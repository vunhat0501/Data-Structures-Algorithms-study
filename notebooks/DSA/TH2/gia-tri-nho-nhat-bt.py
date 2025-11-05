import sys

input = sys.stdin.readline

def tinh_tong():
    try:
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        #* Sap xep mang A tang dan
        a.sort()
        
        #* Sap xep mang B giam dan
        b.sort(reverse=True)
        
        min_p = 0
        for i in range(n):
            min_p += a[i] * b[i]
            
        print(min_p)
        
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