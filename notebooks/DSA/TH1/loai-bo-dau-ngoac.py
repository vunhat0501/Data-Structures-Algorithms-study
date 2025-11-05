import collections
import sys

def is_valid_simple(s: str) -> bool:

    if not s or (len(s) == 1 and s not in '()'):
        return False
        
    balance = 0
    has_paren = False 
    
    for char in s:
        if char == '(':
            balance += 1
            has_paren = True
        elif char == ')':
            balance -= 1
            has_paren = True
        if balance < 0:
            return False
    
    return balance == 0 and len(s) > 1


def solve_test_case(P: str) -> list:

    if is_valid_simple(P):
        return [P]

    queue = collections.deque([P])
    visited = {P}
    solutions = set()
    level_found = False
    
    while queue:
        level_size = len(queue)
        # Bắt đầu duyệt cấp độ hiện tại
        for _ in range(level_size):
            u = queue.popleft()
            
            for i in range(len(u)):
                char = u[i]
                
                # Chỉ loại bỏ dấu ngoặc
                if char == '(' or char == ')':
                    v = u[:i] + u[i+1:] 
                    if v not in visited:
                        if is_valid_simple(v):
                            solutions.add(v)
                            level_found = True 
                        
                        if not level_found:
                            visited.add(v)
                            queue.append(v)

        if level_found:
            break

    # 7. Trả về kết quả
    if not solutions:
        return ["-1"]
    
    return sorted(list(solutions))

def main():
    try:
        T_line = sys.stdin.readline()
        if not T_line: return
        T = int(T_line.strip())
    except:
        return

    results = []
    for _ in range(T):
        try:
            P = sys.stdin.readline().strip()
            if not P: continue
            result = solve_test_case(P)
            results.append(" ".join(result))
            
        except EOFError:
            break
        except Exception:
            continue 
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()