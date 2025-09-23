def permute_recursive(arr, current_perm=[]):
    if not arr:
        print(current_perm)
        return
    
    for i in range(len(arr)):
        chose = arr[i]
        remaining = arr[:i] + arr[i+1:]
        permute_recursive(remaining, current_perm + [chose])
        
def permute_backtrack(arr, start_index):
    if start_index == len(arr):
        print(arr)
        return
    
    for i in range(start_index, len(arr)):
        arr[start_index], arr[i] = arr[i], arr[start_index]
        permute_backtrack(arr, start_index + 1)
        arr[start_index], arr[i] = arr[i], arr[start_index]
        
arr = input("Nhap mang: ").split()
print("Recursive")
permute_recursive(arr)
print("Backtrack")
permute_backtrack(arr, 0)