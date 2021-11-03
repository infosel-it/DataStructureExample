#Example for Factorial by Recursion

def fact(n):
    
    return 1 if (n==1 or n==0) else n * fact(n-1)

num = int(input("enter a number: "))
factVal = fact(5)

print("Factorial of ",num, "is", factVal)