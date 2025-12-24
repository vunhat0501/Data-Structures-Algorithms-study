import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    #* ta cần dùng một mảng parent (hoặc trace) để lưu vết: parent[v] = u nghĩa là "để đến được v, ta đã đi từ u". 
    #* Sau khi tìm thấy đích t, ta lần ngược từ t về s để in ra đường đi.
    
    T = int(next(it))
    for _ in range(T):
        n = int(next(it))
        m = int(next(it))
        s = int(next(it))
        t = int(next(it))
        
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            adj[u].append(v)
            adj[v].append(u)
        
        for i in range(1, n+1):
            adj[i].sort()
        
        visited = [False] * (n+1)
        parent = [0] * (n+1)
        
        def dfs(u):
            visited[u] = True
            if u == t:
                return True
            
            for v in adj[u]:
                if not visited[v]:
                    parent[v] = u #* ghi nho: den v tu u
                    if dfs(v): #* neu nhanh dang di tim thay v thi tra ve True
                        return True
            return False
        
        if dfs(s):
            #* Truy vết đường đi từ t về s
            path = []
            current = t
            while current != 0:
                path.append(current)
                if current == s: #* Đã lùi về đến nơi bắt đầu
                    break
                current = parent[current] #* Lùi về cha của nó
            path.reverse()
            print(*path)
        else:
            print(-1)
    
if __name__ == "__main__":
    solve()