def comb_recursive(arr, k, current_comb=[], start_index=0):
    if len(current_comb) == k:
        print(current_comb)
        return
    
    if start_index == len(arr):
        return
    
    comb_recursive(arr, k, current_comb + [arr[start_index]], start_index + 1)
    
    comb_recursive(arr, k, current_comb, start_index + 1)
    
def comb_backtrack(arr, k, current_comb=[], start_index=0):
    if len(current_comb) == k:
        print(current_comb)
        return
    
    for i in range(start_index, len(arr)):
        current_comb.append(arr[i])
        comb_backtrack(arr, k, current_comb, i + 1)
        
        current_comb.pop()
        
arr = input("Nhap mang: ").split()
k = int(input("Nhap k: "))
print("Recursive")
comb_recursive(arr, k)
print("Backtrack")
comb_backtrack(arr, k)