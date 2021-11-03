#Example for Febonacci

def Fibonacci(n): 
    if n <0 :
        print("Incorrect Input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

num = int(input("enter a number: "))

for i in range(num):
    print(Fibonacci(i))
    

print("Fib Value of number #", num, "is", Fibonacci(num))
