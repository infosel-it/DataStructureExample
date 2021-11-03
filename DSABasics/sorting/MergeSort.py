def mergeSort(inputArray):
    if len(inputArray) >1:
        
        midIndex = len(inputArray)//2
        left = inputArray[:midIndex]
        right = inputArray[midIndex:]
        
        mergeSort(left)
        mergeSort(right)
        
        i=j=k=0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j] :
                inputArray[k] = left[i]
                i += 1
            else :
                inputArray[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            inputArray[k] = left[i]
            i += 1;
            k += 1;
        while j < len(right):
            inputArray[k] = right[i]
            j += 1
            k += 1


def printList(inputArray):
    for i in range(len(inputArray)):
        print(inputArray[i], end ="")
    print()


# Driver Code
if __name__ == '__main__':
    inputArray = [12,11,13,5,6,7]
    print("Input Array", end ="\n")
    printList(inputArray)
    mergeSort(inputArray)
    print("Sorted Array", end ="\n")
    printList(inputArray)