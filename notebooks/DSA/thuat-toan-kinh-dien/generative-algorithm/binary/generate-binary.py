def generate_binary_recursive(n, s=""):
    if n == 0:
        print(s)
        return
    
    generate_binary_recursive(n-1, s+"0")
    generate_binary_recursive(n-1, s+"1")
    
def generate_binary_backtrack(n, s=""):
    if len(s) == n:
        print(s)
        return
    
    generate_binary_backtrack(n, s + '0')
    
    generate_binary_backtrack(n, s + '1')
    
    
n = int(input("Nhap so n: "))
print("Recursive")
generate_binary_recursive(n)
print("Backtrack")
generate_binary_backtrack(n)