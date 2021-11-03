# Row-wise element Addition in Tuple Matrix

X = [[5,3,4],
    [6,1,2],
    [7,8,9]]

Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

result = [map(sum, zip(*t)) for t in zip(X, Y)]

print(result)
