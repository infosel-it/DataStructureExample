def add(input1, input2, action):
    
    print("Input Values", input1 + ', ' + input2)
    print("Input Values %s , %s" % (input1, input2))
    print("input1, input2, action : %(n)s , %(n)s, %(s)s" % {'n': input1, 'n': input2, 's':action})
    print("Input Values {0} , {1}, {2} ".format(input1, input1,action))
    print("Input Values {i1} , {i2}".format(i1=input1, i2=input2))
    
    if action == "add":    
        return input1 + input2
    elif action == "multiply":    
        return input1 * input2

#Driver Code
action = "add"
add("10","20","add")