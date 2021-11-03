import time; 

# Python program for implementation of MergeSort
def mergeSort(inputArr):
    if len(inputArr) > 1:

        # Finding the mid of the array
        mid = len(inputArr)//2

        # Dividing the array elements
        L = inputArr[:mid]

        # into 2 halves
        R = inputArr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Driver Code
if __name__ == '__main__':
    n=100000
    arr = [0] *n 
    for i in range(n): 
        arr[i]=i 
    
#    print ("Before Sort:",arr) 
    startTimeBest = time.time()
    mergeSort(arr) 
    endTimeBest = time.time()
#    print ("After Sort:",arr) 
    
    #print ("Sorted array is:") 
    #for i in range(len(arr)): 
    #    print ("%d" %arr[i]) 
    
    
    #time.sleep(30)
    
    
    print(f"Best Case Runtime of the Program is : {endTimeBest-startTimeBest} seconds")