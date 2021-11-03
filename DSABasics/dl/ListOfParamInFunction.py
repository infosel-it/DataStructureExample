import inspect

def add(input1,input2):
    return input1 + input2

def taxCalculate(netSal,Year, taxPercentage =10, *addtionalInput, **keywords):
    return (netSal//100) * taxPercentage 

# Driver Code
print("Added Value", add(10,20))
print("Calculated Tax Value", taxCalculate(20000,2021,10))
print()
print("...list of parameters name from a function...")
print()
print(inspect.getfullargspec(add))
print()
print(inspect.getfullargspec(taxCalculate))