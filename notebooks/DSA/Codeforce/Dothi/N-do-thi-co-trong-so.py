import sys

INF = 10**9


def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    n = int(next(it))
    m = int(next(it))
    q = int(next(it))
    
    dist = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dist[i][i] = 0
        
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        
        if w < dist[u][v]:
            dist[u][v] = w
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            if dist[i][k] == INF: 
                continue
            
            dik = dist[i][k]
            for j in range(1, n+1):
                if dist[k][j] == INF:
                    continue
                
                dkj = dist[k][j]
                val_via_k = dik if dik > dkj else dkj
                
                if val_via_k < dist[i][j]:
                    dist[i][j] = val_via_k
    
    result = []
    for _ in range(q):
        u = int(next(it))
        v = int(next(it))
        
        res = dist[u][v]
        if res == INF:
            result.append("-1")
        else:
            result.append(str(res))
    print("\n".join(result))
    
if __name__ == "__main__":
    solve()