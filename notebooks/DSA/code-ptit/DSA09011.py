import sys

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    t = int(next(it))
    
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        
        matrix = []
        
        for i in range(n):
            row = []
            for j in range(m):
                row.append(int(next(it)))
            matrix.append(row)
                    
        count = 0
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    count += 1
                    
                    stack = [(i, j)]
                    matrix[i][j] = 0
                    
                    while stack:
                        cx, cy = stack.pop()
                        
                        for k in range(8):
                            nx = cx + dx[k]
                            ny = cy + dy[k]
                            
                            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                                stack.append((nx, ny))
                                matrix[nx][ny] = 0
                                stack.append((nx, ny))
        print(count)
    
if __name__ == "__main__":
    solve()