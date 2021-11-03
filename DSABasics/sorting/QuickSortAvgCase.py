import time; 
import sys

sys.setrecursionlimit(10000)
# Python program for implementation of Quicksort Sort 

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 

    for j in range(low , high): 

        # If current element is smaller than the pivot 
        if arr[j] < pivot: 
        
            # increment index of smaller element 
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 

    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 

        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
        #print ("pi", pi, end="\n") 

        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
        
# Driver code to test above 
if __name__ == '__main__':
    n=2000
    arr = [0] *n 
    maxRange = n-1
    mid = n/2
    
    for i in range(n):
        if(i<mid):
            arr[i]=i
        else:
            arr[i]=maxRange
            maxRange = maxRange-1
    
    print ("Before Sort:",arr) 
    startTimeBest = time.time()
    quickSort(arr,0,n-1) 
    endTimeBest = time.time()
    print ("After Sort:",arr) 
    print(f"Best Case Runtime of the Program is : {endTimeBest-startTimeBest} seconds")

