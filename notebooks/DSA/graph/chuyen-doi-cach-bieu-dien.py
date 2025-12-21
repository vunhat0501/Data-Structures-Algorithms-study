# --- PHẦN 1: TỪ DANH SÁCH CẠNH (EDGE LIST) ---
#* danh sach canh sang danh sach ke
def edge_list_to_adj_list(n, edges):
    adj = [[] for _ in range(n+1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u) #* Bo trong truong hop ma tran co huong
    return adj

#* danh sach canh sang ma tran ke
def edge_list_to_adj_matrix(n, edges):
    matrix = [[0] * (n+1) for _ in range(n+1)]
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1 #* Bo trong truong hop ma tran co huong
    return matrix

# --- PHẦN 2: CHUYỂN ĐỔI QUA LẠI GIỮA MATRIX VÀ LIST ---
#* ma tran ke sang danh sach ke
def adj_matrix_to_adj_list(matrix):
    n = len(matrix) - 1
    adj = [[] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if matrix[i][j] == 1:
                adj[i].append(j)
    return adj

#* danh sach ke sang ma tran ke
def adj_list_to_adj_matrix(n, adj_list):
    matrix = [[0] * (n+1) for _ in range(n+1)]
    
    for u in range(1, n+1):
        for v in adj_list[u]:
            matrix[u][v] = 1
            
    return matrix