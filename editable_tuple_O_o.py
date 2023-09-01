# Change everything after 0 value in a tuple as lists

myTuple = (
    [1, 2],
    [
        3,
    ],
    ["Dont remove me, pop me"],
)  # Tuple with 3 lists

myTuple[1].append(4)  # Will add a 4 to the second list
myTuple[2].pop()  # Will remove last item anyway
myTuple[2].append(
    "is it gone ?"
)  # Will add a new list without the third list wich is question mark

print(myTuple)

"""
printed ([1, 2], [3, 4], [Is it gone ?])
