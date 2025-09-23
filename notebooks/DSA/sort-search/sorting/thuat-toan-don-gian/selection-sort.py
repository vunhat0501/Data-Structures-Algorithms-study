def selection_sort(arr):
	n = len(arr)
	for i in range(n-1):
		
		#* coi phan tu hien tai la phan tu co gia tri nho nhat
		min_idx = i
		
		#* tim kiem phan tu thuc su chua gia tri nho nhat trong day chua duoc sap xep
		for j in range(i+1, n):
			if arr[j] < arr[min_idx]:
				min_idx = j
		
		#* doi cho phan tu len vi tri dung cua no 
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
	return arr

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11, 23, 76, 1]
    
    print("Original array: ", arr)
    
    print("Sorted array: ", selection_sort(arr))