import sys
import random

sys.setrecursionlimit(10000)

def QuickSort(A,left,right):
    if right-1 <=1:
        return()
    
    yellow = left+1
    
    for green in range(left+1,right) :
        if(A[green] <= A[left]) :
            (A[yellow], A[green]) = (A[green],A[yellow])
            yellow = yellow +1
            
    (A[left], A[yellow-1]) = (A[yellow-1], A[left])
    QuickSort(A, left, yellow-1)
    QuickSort(A, yellow,right)
    
def ranomize(l):
    for i in range(len(l)//2):
        j = random.randrange(0,len(l),1)
        k = random.randrange(0,len(l),1)
        (l[j],l[k]) = (l[k],l[j])
        
inl = list(range(7500,0,-1))
#print ("Un Sorted array is:", l)
#print()
ranomize(inl)
#print ("Randomized Sorted array is:", inl)        
QuickSort(inl,0, len(inl))
print ("Sorted array is:", inl)        