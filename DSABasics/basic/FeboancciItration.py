def Fibonacci(number_of_terms):
    a,b = 0,1
    for i in range(number_of_terms):
        a,b = b, a+b
    return a
    
num = int(input("enter a number: "))

for i in range(num):
    print(Fibonacci(i))    

print("Fib Value of number #", num, "is", Fibonacci(num))