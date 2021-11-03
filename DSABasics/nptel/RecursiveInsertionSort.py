

def InsertionSort(seq):
    isort(seq,len(seq))

def isort(seq,k):
    if k >1:
        isort(seq, k-1)
        insert(seq,k-1)
def insert(seq,k):
        pos = k
        while pos >0 and seq[pos] < seq[pos-1]:
            (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
            pos = pos-1
        
arr = [12, 11, 13, 5, 6] 
InsertionSort(arr)
print ("Sorted array is:", arr)

l = list(range(0,5000))
InsertionSort(l)
print ("Sorted array is:", l)
