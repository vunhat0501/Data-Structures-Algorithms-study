import sys
input = sys.stdin.readline

def solve():
    n, m, k = list(map(int, input().split()))
    
    farm = [[0 for _ in range(m)] for _ in range(n)]
    
    max_result = 0
    
    for _ in range(k):
        x, y = list(map(int, input().split()))
        farm[x-1][y-1] = 1
        
    def dfs(row, col):
        if row < 0 or row >= n or col < 0 or col >= m or farm[x][y] == 0:
            return 0
        
        farm[x][y] = 0
        area = 1
        area += dfs(row-1, col)
        area += dfs(row+1, col)
        area += dfs(row, col-1)
        area += dfs(row, col+1)
        return area
    
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                current = dfs(i, j)
                max_result = max(max_result, current)
                
    print(max_result)
    
if __name__ == '__main__':
    solve()