
import sys

class MinHeap:
    
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        print(self.Heap)
        self.Heap[0] = -1 * sys.maxsize
        print( self.Heap[0])
        self.FRONT = 1

def parent(self, pos):
        return pos//2
    
def insert(self, element):
    if(self.size >=self.maxsize):
        return 1
    self.size += 1
    self.Heap[self.size] = element
    current = self.size
    
    while self.Heap[current] < self.Heap[self.parent(current)]:
        self.swap(current, self.parent(current))
        current = self.parent(current)
    

if __name__ == "__main__": 

    print('The minHeap is ')
    minHeap = MinHeap(15)
    minHeap.insert(5)
