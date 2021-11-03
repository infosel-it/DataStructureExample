from assess2.bstnode import minValueNode
class Node:
    def __init__(self, data):#inserting the root node
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
#inserting value into the tree
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
#printing the nodes of the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
 
#to find the lowest value of the tree           
    def minValueNode(self,node):
        current = node
        while(current.left is not None):
            current = current.left
        return current        
    
#to find the avalabiliyy of a number    
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
            
#deleting a Node
def deleteNode(root, key):
    #key s the value to be deleted
    #if tree is empty
    if root is None:
        return root
    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right);
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root

#height of the bst 
def height(bst):
    if bst == None :
        return -1
    else:
        return 1 + max(height(bst.left), height(bst.right))
        
n=int(input("enter the size of tree "))
for i in range(n):
    a=int(input("enter the value to be inserted "))
    if i==0:
        root=Node(a)
    else:
        root.insert(a)
root.PrintTree()
j=1
#enter 1 to insert values, 2 to delete values
#3 to find a value if available,4 to find the height of the tree 
#any other value to print the values of the tree
while j==1:
    j=int(input("enter choice "))
    if j==1:
        a=int(input("enter the value to be inserted "))
        root.insert(a)
    elif j==2:
        a=int(input("enter the value to be deleted "))
        root = deleteNode(root, a)
    elif j==3:
        a=int(input("enter the value to be found "))
        print(root.findval(a))
    elif j==4:
        print("the height of the tree is ")
        h=height(root)
        print(h)
        print("jenisha")
    print("the current tree is ")
    root.PrintTree()
j=int(input("enter 1 to contine "))
