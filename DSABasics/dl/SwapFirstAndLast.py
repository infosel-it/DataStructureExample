def swapFirstAndLastElementInList(iolist):
     iolist[0], iolist[-1] = iolist[-1], iolist[0]
     return iolist
 
 #Driver Code
inputList = [10,20,30,40,50]
print("Actual Input List:",inputList)
swappedList = swapFirstAndLastElementInList(inputList)
print("Swaped Input List:",inputList)