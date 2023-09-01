# Python list comprehensions

vals = [expression for value in collection if condition]

# This is equivalent to:

vals = []
for value in collection:
    if condition:
        vals.append(expression)

# Ex
# x is = 2
even_squares = [x * x for x in range(10) if not x % 2]
# Prints
[0, 4, 16, 36, 64]
