import time 
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
        
# Python Program to Convert seconds 
# into hours, minutes and seconds 
    
# Driver code to test above 
if __name__ == '__main__':
    n=2000
    arr = [0] *n 
    for i in range(n): 
        arr[i]=i 
    newArr = list(reversed(arr))
    
    print ("Before Sort:",newArr) 
    startTimeBest = time.time()
    quickSort(newArr,0,n-1) 
    endTimeBest = time.time()
    totalSec = endTimeBest-startTimeBest
    print ("After Sort:",newArr) 
    print(f"Worst Case Runtime of the Program is : {endTimeBest-startTimeBest} seconds")
