def binarySearch(arr, low, high, key): 
    
    if (high < low): 
        return -1
    mid = (low + high) // 2
    
    if (key == arr[mid]): 
        return mid 
    if (key > arr[mid]): 
        return binarySearch(arr, (mid + 1), high, key) 
    
    return binarySearch(arr, low, (mid - 1), key) 

# Driver code 
# arr = [10, 20, 30, 40, 50 ] 


arr = [5, 6, 7, 8, 9, 10, 12, 60, 70, 80, 90] 

n = len(arr) 
key = 70
pos = binarySearch(arr, 0, n - 1, key) 

print("Searched Index Position", pos)
