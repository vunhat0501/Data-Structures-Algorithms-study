import sys

def dfsRec(adj, visited, s, res):
    visited[s] = True
    res.append(s)
    
    #** visit adjacent vertices that aren't visited yet
    for i in adj[s]:
        if not visited[i]:
            dfsRec(adj, visited, i, res)

def dfs(adj, s):
    visited = [False] * len(adj)
    res = []
    dfsRec(adj, visited, s, res)
    return res

input_data = sys.stdin.read().split('\n')
iterator = iter(input_data)

first_line = next(iterator).split()
v = int(first_line[0])
u = int(first_line[1]) if len(first_line) > 1 else 1 #* mac dinh xuat phat tu mot

adj = [[] for _ in range(v+1)]

#* doc v dong tiep theo, moi dong la cac dinh ke cua  dinh i
for i in range(1, v+1):
    line = next(iterator).split()
    adj[i] = list(map(int, line))
    
#* sap xep neu can duyet tu nho den lon
for i in range(1, v+1):
    adj[i].sort()
    
result = dfs(adj, u)
print(*result)