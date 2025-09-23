def heapify(arr, n, i):
  #* Initialize largest as root
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2
  
  #* If left child is larger than root
  if l < n and arr[l] > arr[largest]:
    largest = l
    
  #* If right child is larger than root
  if r < n and arr[r] > arr[largest]:
    largest = r
    
  #* IF largest isn't root
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    
    heapify(arr, n, largest)
    
def heapSort(arr):
  n = len(arr)
  
  #* Build max heap
  for i in range(n//2-1, -1, -1):
    heapify(arr, n, i)
  
  for i in range(n-1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    heapify(arr, i, 0)
    
  return arr

arr=[12, 11, 13, 5, 6, 7]
heapSort(arr)
print(arr)
