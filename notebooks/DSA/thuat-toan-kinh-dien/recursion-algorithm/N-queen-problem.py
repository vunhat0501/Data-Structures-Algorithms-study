def placeQueens(i, cols, leftDiagonal, rightDiagonal, cur):
    n = len(cols)
    
    #* base case:
    #* if all queens are places, return True
    if i == n:
        return True
    
    #* consider the row and try placing queen in all col one by one
    for j in range(n):
        #* check if queen can be placed
        if cols[j] or rightDiagonal[i+j] or leftDiagonal[i-j+n-1]:
            continue
        
        #* mark the cell occupied
        cols[j] = 1
        rightDiagonal[i+j] = 1
        leftDiagonal[i-j+n-1] = 1
        cur.append(j+1)
        
        if placeQueens(i+1, cols, leftDiagonal, rightDiagonal, cur):
            return True
        
        #* remove the queen from current cell
        cur.pop()
        cols[j] = 0
        rightDiagonal[i+j] = 0
        leftDiagonal[i-j+n-1] = 0
        
    return False

def nQueens(n):
    #* array to mark the occupied cells
    cols = [0] * n
    leftDiagonal = [0] * (n *2)
    rightDiagonal = [0] * (n * 2)
    cur = []
    
    if placeQueens(0, cols, leftDiagonal, rightDiagonal, cur):
        return cur
    else:
        return [-1]
    
n = int(input("Nhap so quan hau: "))
print(nQueens(n))