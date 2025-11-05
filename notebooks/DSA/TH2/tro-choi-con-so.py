import sys

def permutation(n):
    #* Khoi tao mang cac so da dung
    used = [False] * (n + 1)
    
    #* Khoi tao mang luu hoan vi dang tao
    perm = []

    def backtrack():
        #* In ra hoan vi
        if len(perm) == n:
            print(''.join(map(str, perm)))
            return
        
        for i in range(1, n + 1):
            
            #* Kiem tra so da duoc dung chua
            if not used[i]:
                is_valid_to_add = True
                
                #* Neu mang khong rong thi so sanh moi duoc them vao o vong lap truoc
                if len(perm) > 0:
                    last_num = perm[-1] 
                    if abs(i - last_num) == 1:
                        is_valid_to_add = False
                
                if is_valid_to_add:
                    #* Chon so
                    used[i] = True
                    perm.append(i)
                    
                    #* De quy tim so tiep theo
                    backtrack()
                    
                    #* Quay lui
                    perm.pop()
                    used[i] = False

    backtrack()

try:
    input = sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        permutation(n)

except ValueError:
    pass
except EOFError:
    pass