num = int(input("enter a number: "))

factVal = 1

for i in range(1, num+1):
    factVal = factVal * i

print("Factorial of ",num, "is", factVal)


num = int(input("enter a number: "))

factVal = 1
i = 1

while i <= num:
    factVal = factVal * i
    i = i+1
print("Factorial of ",num, "is", factVal)
