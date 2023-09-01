x = "1234567"[6]  # int: 7
y = -round(2.1)  # int: -2
z = (
    x // y
)  # int: -4 (Floor division of this is 3,5 but it rounds up to the prominent round numer)
print(z)  # prints answer: -4

"""
Answer is -4
"""
