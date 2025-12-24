import sys

def solve():
    lines = sys.stdin.readlines()
    
    n = int(lines[0].strip())
    for i in range(n):
        u = i + 1
        if i+1 < len(lines):
            content = lines[i+1].strip().split()
            adj = list(map(int, content))
            adj.sort()
            for v in adj:
                if u < v:
                    print(f"{u} {v}")
    
if __name__ == "__main__":
    solve()