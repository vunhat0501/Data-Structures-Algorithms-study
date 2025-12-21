def solve():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row_string = input()
        grid.append(list(row_string))

    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
