class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        

def insertLevelOrder(arr, root, i, n): 
    if i < n:
        temp = Node(arr[i])
        root = temp
        
        root.left =  insertLevelOrder(arr, root.left, 2*i+1, n)
        root.right =  insertLevelOrder(arr, root.left, 2*i+2, n)

    return root

def inOrder(root): 
    if root != None: 
        inOrder(root.left)  
        print(root.val,end=" ")  
        inOrder(root.right) 

# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    inOrder(root)