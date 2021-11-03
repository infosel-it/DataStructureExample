# Python program to illustrate a Iterator  
  
# creates a empty list 
nums = []  
  
# appending data in list 
nums.append(21) 
nums.append(40.5) 
nums.append("Lab1")
nums.append(100) 
nums.append("Advanced Data Structures") 
nums.append("Python")  

itrObj = iter(nums)

while True:
    try:
        item = next(itrObj)
        print(item)
    except StopIteration:
        break    