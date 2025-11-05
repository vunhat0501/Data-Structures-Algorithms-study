def countingSort(arr, exp1):
    n = len(arr)
    
    #* The output array elements that will have sorted arr
    output = [0] * (n)
    
    #* initialize count array as 0
    count = [0] * (10)
    
    #* Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] // exp1)
        count[index % 10] += 1
    
    #* Change count[i] so that count[i] now contains actual position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i-1]
        #* for example if there are two numbers: 90 and 170 so 2 numbers end with <= 1
        #* their index in output is 1 (first index)
        #* then there are numbers like: 182 and 2 so now we have 4 numbers end with <= 2
        #* their index is 3 (since there are TWO numbers end with 0 in the first index)
    
    #* Build the output array
    i = n-1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        
    #* Copying the output array to arr[], so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
        
def radixSort(arr):
    #* Find the maximum number to know number of digits
    max1 = max(arr)
    
    #* Do counting sort for every digit. Note that instead of passing digit number, exp is passed. 
    #* exp is 10^i where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10
        
    return arr
        
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Sorted array: ", radixSort(arr))