import sys
input = sys.stdin.readline

def solve(n, arr):
    #* khoi tao stack
    stack = []
    Left = [-1] * n
    
    #* duyet i tu 0 den N
    for i in range(0, n):
        #* trong khi stack khong rong va chi so tai phan tu stack.top() <= A[i]: pop stack
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
            
        #* sau khi pop
        #* neu stack con phan tu thi Left[i] = stack.top()
        if stack:
            Left[i] = stack[-1]
        #* neu stack khong con phan tu thi Left[i] = -1
        else:
            Left[i] = -1
            
        stack.append(i)
    
    #* khoi tao lai stack rong
    stack = []
    Right = [-1] * n
    
    #* reverse search
    for i in range(n-1, -1, -1):
        #* trong khi stack khong rong va chi so tai phan tu stack.top() < A[i]: pop stack
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
            
        if stack:
            Right[i] = stack[-1]
        else:
            Right[i] = n
            
        stack.append(i)
    
    sum = 0
    for i in range(n):
        sum += (i -Left[i]) * (Right[i] - i) * arr[i]
    return sum

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))