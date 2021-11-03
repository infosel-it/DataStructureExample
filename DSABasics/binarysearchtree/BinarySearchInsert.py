def insertElement(arr, low, high, key): 
    
    # Find position of element to be deleted 
    pos = findIndexByBST(arr, low, high, key) 
    print("Inserted Index Position", pos)
    
#    if (pos == -1): 
#        print("Element not found") 
#        return n 
        
    # Deleting element 
    n = len(arr)
    print("n", n)
    for i in range(n-1,pos,-1) : 
        arr[i] = arr[i-1] 
    
    arr[pos] = key
    return n - 1

def findIndexByBST(arr, low, high, key): 
    
    mid = (low + high) // 2
    print("Mid", mid)
    if(arr[0] ==0):
        return 0
    else:
        if (arr[mid]==key):
            return -1
    if(arr[mid] <key):
        return findIndexByBST(arr, (mid + 1), high, key)
    if(arr[mid] <key):
        return findIndexByBST(arr, (mid + 1), high, key)

arr = [15, 10, 20, 8, 12, 16, 25]
sortedArr = []
for key in arr:
    sortedArr.append(0)
    n = len(sortedArr) 
#    key = int(input("Enter Number to Insert:"))
    insertElement(sortedArr, 0, n - 1, key) 
    print(sortedArr)