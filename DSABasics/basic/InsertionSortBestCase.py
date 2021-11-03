#Example for Insertion Sort
import sys
import time; 

sys.setrecursionlimit(10000)

def InsertionSort(arr):
     
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        while j >=0 and key <arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key    
        

# Best Case       
n=100000
arr = [0] *n 
for i in range(n): 
    arr[i]=i 

print ("Before Sort:",arr) 
startTimeBest = time.time()
InsertionSort(arr) 
endTimeBest = time.time()
print ("After Sort:",arr) 

#print ("Sorted array is:") 
#for i in range(len(arr)): 
#    print ("%d" %arr[i]) 


#time.sleep(30)


print(f"Best Case Runtime of the Program is : {endTimeBest-startTimeBest} seconds")