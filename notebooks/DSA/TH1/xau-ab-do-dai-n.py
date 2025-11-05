import sys

def solve_ab_string(n):
    result = [''] * n
    all_strings = []

    def backtrack(k):
        if k == n:
            all_strings.append("".join(result))
            return
        
        result[k] = 'A'
        backtrack(k + 1)

        result[k] = 'B'
        backtrack(k + 1)

    backtrack(0)
    
    return all_strings

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    try:
        T = int(data[0])
    except ValueError:
        return

    output = []
    for i in range(1, T + 1):
        if i < len(data):
            try:
                n = int(data[i])
                if 1 <= n <= 10:
                    result_strings = solve_ab_string(n)
                    output.append(" ".join(result_strings))
            except ValueError:
                continue
        else:
            break

    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    main()