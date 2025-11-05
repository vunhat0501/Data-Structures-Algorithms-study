import sys

input = sys.stdin.readline

try:
    n = int(input())

    a = list(map(int, input().split()))

    #* Sap xep mang
    a.sort()
    
    #* TH 3 so duong lon nhat
    prod1 = a[n-1] * a[n-2] * a[n-3]
    
    #* TH 2 so am nho nhat va 1 so duong lon nhat
    prod2 = a[0] * a[1] * a[n-1]
    
    #* TH 2 so duong lon nhat
    prod3 = a[n-1] * a[n-2]
    
    #* TH 2 so am nho nhat
    prod4 = a[0] * a[1]
    
    #* Tim tich lon nhat
    result = max(prod1, prod2, prod3, prod4)
    
    print(result)

except ValueError:
    pass
except EOFError:
    pass