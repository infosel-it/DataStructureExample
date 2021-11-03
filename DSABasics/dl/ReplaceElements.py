import numpy as np

print("===Replace Elements Using < , > operator===")
io_arr = np.array([75.42436315, 42.48558583, 60.32924763])
print("Given array:")
print(io_arr)

print("\nReplace all elements of array which are greater than 55. to 35.500001")
io_arr[io_arr > 55] = 35.500001

print("Modified array:")
print(io_arr)
print()
print("===Replace Elements Using where condition===")

twoDimArr = np.array([[45, 52, 10],
                  [1, 5, 25]])

print("Given array:")
print(twoDimArr)
print("\nReplace all elements of array which are \
greater than or equal to 25 to 250")  
print("else 50 ")

print(np.where(twoDimArr >= 25, 250, 50))
print()