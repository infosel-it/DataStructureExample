def palindrome(inputString):
    length = len(inputString)
    midIndex = (length-1)//2
    start = 0
    last = length-1
    isPalindrome = 0
    
    while(start<midIndex):
        if(inputString[start] == inputString[last]):
            start +=1
            last -=1
        else:
            isPalindrome = 1
            break;
    return isPalindrome
        
def symmetric(inputString):      
    length = len(inputString)
    isSymmetric = 0
    
    if length%2:
        midIndex = length //2 +1
    else:
        midIndex = length//2    
        
    startIndex1 = 0
    startIndex2 = midIndex
    
    while(startIndex1 < midIndex and startIndex2 < length):
        if(inputString[startIndex1] == inputString[startIndex2]):
            startIndex1 = startIndex1 +1
            startIndex2 = startIndex2 +1
        else:
            isSymmetric = 1
            break
    return isSymmetric

# Driver Code
#ioString = 'amaama'

ioString = input("Enter Input String: ") 
      
isPalindrome = palindrome(ioString)
isSymmetric = symmetric(ioString)
if isPalindrome == 0 and isSymmetric == 0 :
    print("The input string is both Symmetric and Palindrome")
elif isPalindrome == 0:
    print("The input string is Palindrome")
elif isSymmetric == 0:
    print("The input string is Symmetric")     
else:
    print("The input string is neither Palindrome or Symmetric")   