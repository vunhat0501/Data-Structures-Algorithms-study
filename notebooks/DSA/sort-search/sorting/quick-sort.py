import random

def partition(arr, low, high):
	#** Generate random index in sub-array and swap its element with the last element
  random_index = random.randint(low, high)
  arr[random_index], arr[high] = arr[high], arr[random_index]
    
  pivot = arr[high]
  i = low - 1
  
  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      swap(arr, i, j)
      
  swap(arr, i + 1, high)
  return i+1

def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]
  
def quick_sort(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    
    quick_sort(arr, low, pi - 1)
    quick_sort(arr, pi + 1, high)


arr = [int(x) for x in input().split()]
quick_sort(arr, 0, len(arr) - 1)
print(arr)