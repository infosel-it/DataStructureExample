
#Example for Loops

import keyword 


# Iterating with integer range value
for step in range(5):
        print((step))
        


''' Iterating an Array and value accessing by index value. 
Keywords of Python is collected in 'keys' array'''
print(" ### Iterating and Accessing array by index ###")    
keys = keyword.kwlist
for i in range(len(keys)):
    print(keys[i], end = " ")
    
print();

# Iterating an Array. Keywords of Python is collected in 'keys' array
print(" ### Iterating an array ###", end ="\n")    
for key in keys:
    print(key, end =" ")
    