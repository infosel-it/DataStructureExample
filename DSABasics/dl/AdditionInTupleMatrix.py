io_list1 = [[('a', 5), ('b', 5)], [('c', 3)], [('d', 2), ('e', 7)]]
print("The original list is : " + str(io_list1))

io_list2 = [10, 20, 30]

res = [[(idx, val) for idx in key] for key,  val in zip(io_list1, io_list2)]

print("The matrix after row elements addition : " + str(res)) 
