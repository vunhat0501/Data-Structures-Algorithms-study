import sys

def bieu_thuc(nums, used, count, current_value):
    #* Kiem tra neu ket qua sau khi dung ca 5 so
    if count == 5:
        return current_value == 23
    
    for i in range(5):
        
        #* Neu so i chua duoc dung => them vao danh sach de dung
        if not used[i]:
            num_to_add = nums[i]
        
            #* Danh dau so i la da dung
            used[i] = True
            
            #* Neu day bat dau = 0, chi gan no lam gia tri khoi dau
            if count == 0:
                if bieu_thuc(nums, used, count + 1, num_to_add):
                    return True
            
            else:
                #* Cong
                if bieu_thuc(nums, used, count + 1, current_value + num_to_add):
                    return True
                
                #* Tru
                if bieu_thuc(nums, used, count + 1, current_value - num_to_add):
                    return True
                
                #* Nhan
                if bieu_thuc(nums, used, count + 1, current_value * num_to_add):
                    return True
                
            #* Bo danh dau de chuyen so khac lam gia tri khoi dau
            used[i] = False
    return False

try:
    input = sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        nums = list(map(int, input().split()))
        used = [False] * 5 
        
        if bieu_thuc(nums, used, 0, 0):
            print("YES")
        else:
            print("NO")

except ValueError:
    pass
except EOFError:
    pass