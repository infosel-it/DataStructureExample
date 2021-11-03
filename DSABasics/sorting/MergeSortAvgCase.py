import time

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
                inputArr[k] = L[i]
                i += 1
            else:
                inputArr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            inputArr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            inputArr[k] = R[j]
            j += 1
            k += 1

# Code to print the list

# Driver Code
if __name__ == '__main__':
    n=100000
    firstArr = [0] *n 
    maxRange = n-1
    mid = n/2
    
    for i in range(n):
        if(i<mid):
            firstArr[i]=i
        else:
            firstArr[i]=maxRange
            maxRange = maxRange-1
        
#    print ("Before Sort:",firstArr) 
    print ("Before Sort:") 
    for i in range(49990,50010,1): 
        print ("%d" %firstArr[i],end =",")
    print()    
    startTimeAvg = time.time()
    mergeSort(firstArr) 
    endTimeAvg = time.time()
#    print ("After Sort:",firstArr) 
    print ("After Sort:")
#    print ("After Sort:",newArr) 
    for i in range(100): 
        print ("%d" %firstArr[i],end =",")
    print()    
    print(f"Worst Case of the Program is : {endTimeAvg-startTimeAvg} seconds" )