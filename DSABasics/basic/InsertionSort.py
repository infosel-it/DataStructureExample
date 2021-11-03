#Example for Insertion Sort
import datetime; 


def InsertionSort(arr):
     
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        while j >=0 and key <arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key    
        
        
ct = datetime.datetime.now()
ts = ct.timestamp() 

arr = [12, 11, 13, 5, 6] 
InsertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]) 