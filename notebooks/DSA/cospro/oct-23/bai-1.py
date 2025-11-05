import math

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def cal_index_sum(m, input_arr):
    arr = selection_sort(input_arr)
    # print("sorted arr: ", arr)
    n = len(arr)
    
    sum = 0
    for i in range(m, n, m):
        sum += arr[i]
    
    return sum

number_string = input()
number_list = list(map(int, number_string.split(",")))
m = int(input("Nhap m: "))
print(cal_index_sum(m, number_list))