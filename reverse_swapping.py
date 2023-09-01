x = 30
y = 40
z = 50

print("Before swap:")
print("x =", x)
print("y =", y)
print("z =", z)

x, y, z = z, y, x  # swap values in reverse order

print("\nAfter swap:")
print("x =", x)
print("y =", y)
print("z =", z)

### Can also look like this

"""
-->
x, y, z = [1, 2, 3]
x, y, z = ([1, ], [2, ], [3])
<--
"""

### End
