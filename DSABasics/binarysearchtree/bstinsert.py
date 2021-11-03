def insertSorted(arr, n, key, capacity): 
    
    if (n >= capacity): 
        return n 

    i = n - 1
    while i >= 0 and arr[i] > key: 
        print("i",i , "key", key, "arr[i]", arr[i])
        arr[i + 1] = arr[i] 
        i -= 1

    arr[i + 1] = key 

    return (n + 1) 

# Driver Code 
#arr = [12, 16, 75, 80, 90, 100] 

arr = [12] 

for i in range(10): 
    arr.append(0) 

capacity = len(arr) 
print(capacity)
n = 2
key = 10

print("Before Insertion: ", end = " "); 
for i in range(n): 
    print(arr[i], end = " ") 
    
# Inserting key 
n = insertSorted(arr, n, key, capacity) 

print("\nAfter Insertion: ", end = "") 
for i in range(n): 
    print(arr[i], end = " ") 

# This code is contributed by Mohit Kumar 
