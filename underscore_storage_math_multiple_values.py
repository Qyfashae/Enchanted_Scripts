data = [
    (1, "one"),
    (2, "two"),
    (3, "three"),
]  # Every listTuple holds a integer and a string.
for _, word in data:  # The '_' will act as the first integer in EVERY keyholder
    print(word)  # Print will be (1, 'one'), (2, 'two'), (3, 'three')
