#Example for Lambda

ages = [13, 90, 17, 59, 21, 60, 5, 70, 80] 

adults = list(filter(lambda age: age>18 and age<65, ages)) 

print(adults)

seniorCitizon = list(filter(lambda age: age>65, ages)) 

print(seniorCitizon)
