import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, m = list(map(int, input().split()))
    
    adj= [[] for _ in range(n)]
    for _ in range(m):
        u, v = list(map(int, input().split()))
        adj[u-1].append(v-1 )
        
    visited = [False] * n
    
    def bfs(start, end):
        queue = deque([start])
        visited[start] = True