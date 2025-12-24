import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    
    it = iter(data)
    
    n = int(next(it))
    k = int(next(it))
    
    #* khoi tao danh sach phong thoat hiem
    exits = []
    for _ in range(k):
        exits.append(int(next(it)))
        
    #* danh sach adj
    m = int(next(it))
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        x = int(next(it))
        y = int(next(it))
        adj[x].append(y)
        adj[y].append(x)
    
    #* khoi tao mang chua phong chua tham
    dist = [-1] * (n+1)
    
    queue = deque()
    
    #* duyet qua danh sach exit va danh cac phong exit = True va dua vao queue
    for exit in exits:
        dist[exit] = 0
        queue.append(exit)
        
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    
    print(*dist[1:])
    
if __name__ == "__main__":
    solve()