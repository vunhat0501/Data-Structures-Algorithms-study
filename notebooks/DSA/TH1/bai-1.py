import sys
input = sys.stdin.read

def multiply_matrix(a, b, mod):
    #* Nhan ma tran 4x4
    c = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % mod
    return c

def power_matrix(m, p, mod):
    #* tinh m^p bang luy thua nhi phan
    #* Ma tran don vi 4x4
    identity = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
    if p == 0:
        return identity
    if p == 1:
        return m
    
    res = power_matrix(m, p // 2, mod)
    res = multiply_matrix(res, res, mod)
    
    if p % 2 == 1:
        res = multiply_matrix(res, m, mod)
    return res

def tribonacci_sum(n):
    mod = 10**15 + 7
    
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n == 3:
        return 6

    #* Ma tran chuyen doi M 
    m = [[1, 1, 1, 0], 
         [1, 0, 0, 0],
         [0, 1, 0, 0],
         [1, 0, 0, 1]]
    
    #* Vector ban dau V_3 = [T(4), T(3), T(2), F(3)]^T
    v3 = [6, 3, 2, 6]

    m_pow = power_matrix(m, n - 3, mod)
    
    result_sum = 0
    for i in range(4):
        result_sum = (result_sum + m_pow[3][i] * v3[i]) % mod
        
    return result_sum

def main():
    data = input().split()
    if not data:
        return
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        results.append(str(tribonacci_sum(N)))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()