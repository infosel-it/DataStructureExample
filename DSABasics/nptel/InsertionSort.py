def InsertionSort(seq):
    for sliceEnd in range(len(seq)):
        pos = sliceEnd
        while pos >0 and seq[pos] < seq[pos-1]:
            print("1")
            (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
            pos = pos-1
        
arr = [15,20,4,6,9,25,32,40,3,1] 
InsertionSort(arr)
print ("Sorted array is:", arr)


