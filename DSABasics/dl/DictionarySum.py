#Python program to find the sum of all items in a dictionary
def DictSum(ipDict):
    
    totalSum = 0
    for i in ipDict.values():
        totalSum = totalSum + i
    
    return totalSum

# Driver Function
ipDict = {'Emp1': 10000, 'Emp2':20000, 'Emp3':25000}
print("Sum of All Items in Dictionary :", DictSum(ipDict))
