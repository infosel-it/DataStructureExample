#Example for Insertion Sort
import time; 

def InsertionSort(arr):
     
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        while j >=0 and key <arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key    
        

# Worst Case       

n=10000
firstArr = [0] *n 

maxRange = n-1
mid = n/2

for i in range(n):
    print(i) 
    if(i<mid):
        firstArr[i]=i
    else:
        firstArr[i]=maxRange
        maxRange = maxRange-1
    
print ("Before Sort:",firstArr) 
startTimeAvg = time.time()
InsertionSort(firstArr) 
endTimeAvg = time.time()
print ("After Sort:",firstArr) 


print(f"Worst Case of the Program is : {endTimeAvg-startTimeAvg} seconds" )