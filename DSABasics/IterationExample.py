
#Example for Iteration

import keyword 


for step in range(5):
        print((step))
        

keys = keyword.kwlist

for i in range(len(keys)):
    print(keys[i], end = " ")
    

# printing a element in same line
a = [1, 2, 3, 4] 
for i in range(4): 
    print(a[i], end = "#")  
    
    