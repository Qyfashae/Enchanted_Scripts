tupleOne = (["1"], ["2"], ["3"])
tupleTwo = ("1", "2", ("3", "4", "str"), "6")

print(tupleOne, "tupleOne") # Printed: ?
tupleOne[1].append(3)
tupleOne[2].append(2)
print(tupleOne, "tupleOne") # Printed: ?
print(tupleTwo[2][0], ": tupleTwo innerPrint") # Printed: ?
print(tupleTwo[2][1], ": tupleTwo, innerPrint") # Printed: ?
print(tupleTwo, "tupleTwo") # Printed: ?

if (tupleOne == tupleOne) or (tupleTwo == tupleTwo):
    tupleThree = tupleOne + tupleTwo
    print(tupleThree) # Printed: ?
    x = list(tupleThree)
    x[1] = 2
    y = list(tupleOne)
    y[0] = 11
    z = list(tupleTwo)
    z = "???"
    print(tupleThree) # Printed: ?
    tupleThree = x
    tupleOne = y
    tupleTwo = z
    tuples = x, y, z
    print(tuples) # Printed: ?
