# Python program to illustrate a array  
  
# creates a empty list 
nums = []  
  
# appending data in list 
nums.append(21) 
nums.append(40.5) 
nums.append("Lab1")
nums.append(100) 
nums.append("Advanced Data Structures") 
  
# Array Delete
print ("The list before deleting any value") 
print (nums) 
# using del to delete 2nd element of list 
del nums[1] 
# printing list after deleting 2nd element 
print ("The list after deleting 2nd element") 
print (nums) 


#Insert an element to array
print ("The list after inserting element at index 3") 
nums.insert(2, 10)
print (nums) 

#Looping a array
for data in nums:
    print(data)