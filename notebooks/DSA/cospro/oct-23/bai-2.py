def solution(n, watering_can, m):
    #** Khoi tao khu vuon N*N voi moi o deu chua duoc tuoi nuoc (=0)
    garden = [[0 for _ in range(n)] for _ in range(n)]
    
    #** Lap qua tung voi phun
    for sprinkler in watering_can:
        #** Khoi tao voi
        r, c, strength = sprinkler
        
        #** Danh dau cac vi tri duoc tuoi nuoc
        
        #** Kiem tra xem voi tuoi co nam trong vuon khong 
        if 0 <= r < n and 0 <= c < n:
            garden[r][c] = 1
            
        #** Kiem tra 4 huong cua voi nuoc
        for i in range(1, strength+1):
        #** Kiem tra huong tren (giam hang)
            if 0 <= r - i < n:
                garden[r-i][c] = 1
            
        #** Kiem tra huong duoi (tang hang)
            if 0 <= r + i < n:
                garden[r+i][c] = 1
                
        #** Kiem tra ben trai (giam cot)
            if 0 <= c - i < n:
                garden[r][c-i] = 1
                
        #** Kiem tra ben phai (tang cot)
            if 0 <= c + i < n:
                garden[r][c+i] = 1
                
    #** Dem nhung o chua duoc tuoi (=0)
    count = 0
    for row in garden:
        for cell in row:
            if cell == 0:
                count += 1
    
    return count

n = 5
m = 2
watering_can = [
    [0, 0, 1],  
    [2, 2, 2]  
]

print(solution(n, watering_can, m))