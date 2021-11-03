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
arr = [0] *n 

for i in range(n): 
    arr[i]=i
newArr = list(reversed(arr))

#print ("Before Sort:",newArr) 
#for i in range(100): 
#    print ("%d" %newArr[i],end =",") 
startTimeWorst = time.time()
InsertionSort(newArr) 
endTimeWorst = time.time()
#print ("After Sort:",newArr) 
#for i in range(100): 
#    print ("%d" %newArr[i],end =",") 


print(f"Worst Case of the Program is : {endTimeWorst-startTimeWorst} seconds")